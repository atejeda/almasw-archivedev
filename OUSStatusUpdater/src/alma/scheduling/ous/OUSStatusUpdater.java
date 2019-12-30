package alma.scheduling.ous;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.apache.commons.cli.BasicParser;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;

import alma.entity.xmlbinding.ousstatus.OUSStatus;
import alma.entity.xmlbinding.ousstatus.SessionT;
import alma.entity.xmlbinding.valuetypes.ExecBlockRefT;
import alma.lifecycle.persistence.StateArchive;
import alma.lifecycle.stateengine.constants.Subsystem;
import alma.scheduling.factory.StateSystemContextFactory; 

/*
  select
      e.sessionuid session_uid,
      o.status_entity_id mousstatus_uid,
      e.sessionpartid,
      e.execblockuid execblock_uid,
      to_char(e.starttime, 'YYYY-MM-DD HH24:MI:SS.FF') starttime,
      to_char(e.endtime, 'YYYY-MM-DD HH24:MI:SS.FF') endtime,
      e.obsprojectcode obsproject_code,
      s.domain_entity_id schedblock_uid,
      s.status_entity_id sbstatus_uid,
      o.domain_entity_state mous_status,
      s.domain_entity_state schedblock_status,
      o.flags mous_flags,
      s.flags schedblock_flags,
      e.almabuild
  from 
      alma.sched_block_status s, alma.obs_unit_set_status o, alma.aqua_v_execblock e
  where 
      s.parent_obs_unit_set_status_id = o.status_entity_id and
      e.schedblockuid = s.domain_entity_id and 
      o.status_entity_id != e.sessionuid and
      to_char(starttime, 'YYYY-MM-DD-HH24:MI:SS') > '2018-10-15-06:33' and
      to_char(starttime, 'YYYY-MM-DD-HH24:MI:SS') < '2018-10-23-18:16' and
      e.almabuild = 'ONLINE-CYCLE6-B-59-2018-10-17-28-00-00' and
      e.obsprojectcode not like '%CSV';
*/

public class OUSStatusUpdater {
	
	public static void main(String[] args) throws Exception {
		// parser
		
		Options options = new Options();
		options.addOption("f", "file", true, "The file.csv to use");
		options.addOption("t", "time", false, "Set endtime to date.now for sessions endtime unset with more than 1 EB");
		options.addOption("p", "persist", false, "Setting this will the application will persist the changes");
		options.addOption("h", "help", false, "Display the help");

		CommandLineParser parser = new BasicParser();
		CommandLine cmd = parser.parse(options, args);
		HelpFormatter formatter = new HelpFormatter();

		// option values
		
		if (!cmd.hasOption("f") || cmd.hasOption("h")) {
			formatter.printHelp("OUSStatusUpdater", options);
			return;
		}

		final String csvFile = cmd.getOptionValue("f");
		final boolean timeNow = cmd.hasOption("t");
		final boolean persist = cmd.hasOption("p");

		System.out.println(String.format("file  = %s ", csvFile));
		System.out.println(String.format("time  = %s ", timeNow));
		System.out.println(String.format("persist = %s ", persist));

		// reading

		DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");

		System.out.println("Invoking the state archive...");
		//System.setProperty("ACS.data", "/alma/ACS-current/acsdata/");
		StateArchive stateArchive = StateSystemContextFactory.getInstance().getStateArchive();

		System.out.println(String.format("about to read %s", csvFile));
		
		List<String> failed = new ArrayList<>();
		List<String> time = new ArrayList<>();

		try (BufferedReader br = new BufferedReader(new FileReader(new File(csvFile)))) {
			String line;
			while ((line = br.readLine()) != null) {
				String fields[] = line.split(",");

				String sessionUid = fields[0];
				String ousStatusUid = fields[1];
				String sessionPartId = fields[2];
				String execBlockUid = fields[3];
				String execBlockStart = fields[4];
				String execBlockEnd = fields[5];
				String sbUid = fields[7];
				String sbStatusUid = fields[8];

				System.out.println("> processing...");

				System.out.println(String.format("session uid  = %s", sessionUid));
				System.out.println(String.format("ous status uid  = %s", ousStatusUid));
				System.out.println(String.format("session part id = %s", sessionPartId));
				System.out.println(String.format("execblock uid  = %s", execBlockUid));
				System.out.println(String.format("execblock start  = %s", execBlockStart));
				System.out.println(String.format("execblock end  = %s", execBlockEnd));
				System.out.println(String.format("schedblock uid = %s", sbUid));
				System.out.println(String.format("schedblock status uid = %s", sbStatusUid));

				System.out.println("> retrieving ous status...");
				
				try {
					// ous

					OUSStatus[] statuses = stateArchive.getOUSStatusList(new String[] { ousStatusUid });

					if (statuses == null || statuses.length < 1)
						throw new RuntimeException("ous not found...");

					OUSStatus ouss = statuses[0];

					// session

					System.out.println("> Reading sessions...");
					System.out.println(String.format("contains %d sessions ", ouss.getSession().length));

					SessionT session = null;
					for (final SessionT sessionType : ouss.getSession()) {
						if (sessionType.getEntityPartId().equals(sessionPartId)) {
							session = sessionType;
							break;
						}
					}
					
					if (session == null)
						throw new RuntimeException("session for partid not found...");

					if (!session.getSBStatusRef().getEntityId().equals(sbStatusUid))
						throw new RuntimeException("the schedblock doesnt belong to this session?");

					// execution blocks

					System.out.println(String.format("%s contains #%d execblocks (before)", 
							session.getEntityPartId(), session.getExecBlockRef().length));

					for (ExecBlockRefT ebref : session.getExecBlockRef()) {
						if (ebref.getExecBlockId().equals(execBlockUid))
							throw new RuntimeException("exec block already exists in this session/part");
					}

					final ExecBlockRefT ebref = new ExecBlockRefT();
					ebref.setExecBlockId(execBlockUid);
					session.addExecBlockRef(ebref);

					System.out.println(String.format("%s added to (part id) %s for MOUS %s", 
							execBlockUid, session.getEntityPartId(), ouss.getOUSStatusEntity().getEntityId()));

					System.out.println(String.format("%s contains #%d execblocks (after)", 
							session.getEntityPartId(), session.getExecBlockRef().length));
					
					// endtime

					if (session.getExecBlockRef().length > 1) {
						if (timeNow) {
							session.setEndTime(dateFormat.format(new Date()));
						} else {
							time.add(String.format("ous status = %s, part id = %s",
									ouss.getOUSStatusEntity().getEntityId(), session.getEntityPartId()));
						}
					} else {
						session.setEndTime(dateFormat.format(dateFormat.parse(execBlockEnd)));
					}

					// persist

					if (persist) {
						stateArchive.insertOrUpdate(ouss, Subsystem.SCHEDULING);
						System.out.println("> persisted...");
					} else {
						System.out.println("> dry run");
					}

				} catch (Exception e) {
					failed.add(ousStatusUid);
					System.out.println("> there's a problem... ");
					e.printStackTrace(System.out);
				} finally {
					System.out.println("> done...");
					System.out.println("--------------------------------------------------");
				}
			}
		}

		// summary

		System.out.println("Summary...");
		failed.stream().forEach(e -> {
			System.out.println(String.format("> Couldn't find or process ous status %s", e));
		});
		time.stream().forEach(e -> {
			System.out.println(String.format("> Couldn't compute time for %s, check -t option...", e));
		});
	}
}
