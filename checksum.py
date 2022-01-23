from rich.console import Console
import subprocess
import difflib as dl

def main():
    c = Console()
    def line():
        c.print("_", style="underline", justify="center")

    line()
    path = c.input("| Path: ")
    host_hash = c.input("| Insert the SHA256 hash provided by host: ")
    
    local_hash = subprocess.Popen(["sha256sum", path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    format_hash = str(local_hash.stdout.read()).split("/", 1)[0].split("'", 1)[1].strip()

    if format_hash == host_hash:
        c.print("| Equal SHA256, safe to use", style="green blink bold")
        line()
    else:
        c.print("| Warning! this file has been compromised", style="blink bold yellow")
        diff_input = c.input("| Do you want to see the difference between the sums? (y/N): ").lower()

        if diff_input == "y" or diff_input == "yes":
            for diff in dl.context_diff(host_hash, format_hash):
                c.print(diff)
        else:
            pass

        line()

if __name__ == "__main__":
    main()