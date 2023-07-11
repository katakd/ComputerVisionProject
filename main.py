import argparse, subprocess

parser = argparse.ArgumentParser("SSL methods")
parser.add_argument("--method",
                    type=str,
                    default="fixmatch",
                    help="method name")
args = parser.parse_args()

methods = {
    "fixmath": "bash fixmatch.sh",
    "noisy student": "bash noisy.sh",
    "pseudo label": "bash pseudo.sh",
    "pi": "bash pi.sh"
}
assert args.method in methods, f"Method {args.method} not implemented in {methods}"


print(f"Training with default configuration of method: {args.method}")
subprocess.run(methods[args.method], shell=True)
