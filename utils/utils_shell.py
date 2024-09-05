import subprocess
from utils import run_task as rt
from cmd2 import CommandSet, with_default_category


@with_default_category("Utils")
class UtilsCommandSet(CommandSet):
    def __init__(self):
        super().__init__()

    def do_clear(self, arg):
        "Clear screen"
        subprocess.run(["clear"], shell=True)

    def do_show_processes(self, arg):
        "Show current running processes"
        rt.showRunningProcs()

    def do_show_process_data(self, arg):
        "Show specific process output (Log Location: /tmp/netspion/processes/)"
        rt.showProcessData(int(arg))

    def do_exec_mode(self, arg):
        "Set execution mode (N: run task in new terminal) / (B: run task in background)"
        self.mode = arg

    def do_end_process(self, arg):
        "End specific process"
        rt.endProcess(int(arg))
