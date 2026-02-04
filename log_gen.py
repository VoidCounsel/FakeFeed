import time
import random
from datetime import datetime

# ────────────────────────────────────────────────
# ANSI COLORS
# ────────────────────────────────────────────────
RESET = "\033[0m"
COLORS = {
    "INFO":     "\033[36m",      # cyan
    "DEBUG":    "\033[90m",      # bright black / gray
    "TRACE":    "\033[90m",
    "NOTICE":   "\033[35m",      # magenta
    "WARN":     "\033[33m",      # yellow
    "ERROR":    "\033[31;1m",    # bright red
    "CRITICAL": "\033[31;1m\033[1m",  # bold bright red
}
DIM = "\033[2m"      # dim for host / service
BRIGHT = "\033[1m"

# ────────────────────────────────────────────────
# WORD LISTS
# ────────────────────────────────────────────────
LOG_LEVELS = ["INFO", "WARN", "ERROR", "DEBUG", "CRITICAL", "TRACE", "NOTICE"]

SERVICES = [
    "auth-gateway", "iam-core", "token-validator", "policy-engine",
    "kubelet", "etcd-watch", "control-plane", "sidecar-proxy",
    "otel-collector", "prom-scraper", "alert-dispatcher", "chaos-agent",
    "vector-agent", "fluent-bit", "filebeat", "metricd", "trivy-scanner",
]

HOSTS = [
    "node-07a", "k8s-worker-42", "ip-172-31-94-112", "ec2-i-0f8d3e2a1b9c4d5e",
    "rke2-master-3", "aks-agentpool-12457890-vmss00000p", "pod-ip-10-244-3-189",
    "gke-g1-small-xyz-789f", "minikube", "kind-control-plane",
]

ACTION_VERBS = [
    "processing", "validating", "rejecting", "authorizing", "refreshing",
    "syncing", "reconciling", "evicting", "terminating", "scaling",
    "restarting", "rolling", "draining", "retrying", "failing", "throttling",
]

OBJECTS = [
    "JWT", "access-token", "refresh-token", "pod", "deployment", "statefulset",
    "node", "namespace", "secret", "configmap", "ingress", "service", "pvc",
]

SUFFIXES = [
    "succeeded", "failed", "timed-out", "denied", "accepted", "completed",
    "dropped", "queued", "retried (3)", "status=200", "status=429",
]

ERROR_PATTERNS = [
    "connection refused", "TLS handshake timeout", "certificate expired",
    "invalid signature", "audience mismatch", "rate limit exceeded",
    "upstream timeout", "out of memory", "etcdserver: request timed out"
]

# ────────────────────────────────────────────────
# LOADING BAR – single style, fixed borders
# ────────────────────────────────────────────────
LOAD_ADVERBS = [
    "quantumly", "tachyonically", "chronitonically", "zeropointly", "subspacely",
    "temporally", "entropically", "nonlocally",
    "fractally", "holographically", "topologically", "acausally", "retrocausally",
]

LOAD_VERBS = [
    "Entangling", "Collapsing", "Calibrating", "Synchronizing", "Decrypting",
    "Re-aligning", "Harvesting", "Folding", "Initializing", "Purging",
    "Compressing", "Tuning", "Stabilizing", "Bootstrapping", "Resolving",
    "Amplifying", "Transmuting", "Vectorizing", "Quantizing", "Phase-shifting",
]

LOAD_OBJECTS = [
    "flux capacitor", "field harmonics", "membrane tension", "telemetry entropy",
    "hash oracle", "singularity bootstrap", "probability threads", "causal knot",
    "dimensional anchor", "vacuum decay bubble", "topological defect",
    "entanglement manifold", "wavefunction collapse", "axion condensate",
]

def generate_loading_task():
    adverb = random.choice(LOAD_ADVERBS)
    verb = random.choice(LOAD_VERBS).lower()
    obj = random.choice(LOAD_OBJECTS)
    suffix = random.choice(["", " matrix", " core", " lattice", " field", " conduit"]) if random.random() < 0.5 else ""
    extra = random.choice(["", " in subspace", " via hyperspace", " at Planck resolution"]) if random.random() < 0.35 else ""

    task = f"{adverb} {verb} {obj}{suffix}{extra}"
    task = task[0].upper() + task[1:]
    return task

def print_fake_loading_bar():
    task = generate_loading_task()
    
    # Bar width
    bar_width = random.randint(38, 56)
    
    # Inner content width = bar + space before % + "100%" + space after
    inner_width = bar_width + 7   # ' ' + '100%' + ' ' = 7 chars
    
    # Horizontal line of correct length
    hline = "─" * inner_width
    
    # Top border
    print(f"\n{BRIGHT}╭─ {task.ljust(inner_width - 4)} ─╮{RESET}")
    
    current_progress = 0.0
    last_filled = -1
    style_char = random.choice(["█", "▓", "▉", "▊", "■"])
    empty_char = random.choice([" ", "·", "░"])

    for step in range(random.randint(18, 36)):
        remaining = 1.0 - current_progress
        increment = remaining * random.uniform(0.07, 0.26)
        if random.random() < 0.22:
            increment *= random.uniform(2.5, 7.0)
        if random.random() < 0.35:
            increment *= random.uniform(0.05, 0.4)

        current_progress += increment
        current_progress = min(1.0, current_progress)

        filled = int(bar_width * current_progress)
        percent = int(current_progress * 100)

        if filled == last_filled and step < 35:
            time.sleep(random.uniform(0.05, 0.4))
            continue

        bar = style_char * filled + empty_char * (bar_width - filled)
        line = f"{BRIGHT}│{RESET} {bar} {percent:>3}% {BRIGHT}│{RESET}"
        print(line, end="\r", flush=True)
        last_filled = filled

        sleep_time = random.uniform(0.05, 0.7)
        if current_progress > 0.88:
            sleep_time *= random.uniform(0.7, 3.0) if random.random() < 0.6 else random.uniform(1.4, 4.2)
        time.sleep(max(0.03, sleep_time))

    # Final bar
    bar = style_char * bar_width
    print(f"{BRIGHT}│{RESET} {bar} 100% {BRIGHT}│{RESET}")
    
    # Bottom border
    print(f"{BRIGHT}╰{'─' * inner_width}╯{RESET}\n")
    
    time.sleep(random.uniform(0.12, 0.55))

# ────────────────────────────────────────────────
# LOG HELPERS
# ────────────────────────────────────────────────
def random_timestamp():
    now = datetime.utcnow()
    ms = random.randint(0, 999)
    jitter = random.uniform(-1.2, 1.8)
    ts = now.timestamp() + jitter
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%Y-%m-%d %H:%M:%S") + f".{ms:03d}Z"

def random_duration():
    kinds = [
        f"{random.randint(8, 1200)}ms",
        f"{random.uniform(0.4, 5.9):.2f}s",
        f"{random.randint(90, 6800)}µs"
    ]
    return random.choice(kinds)

def build_message():
    style = random.random()
    if style < 0.40:
        parts = [
            random.choice(SERVICES),
            random.choice(ACTION_VERBS),
            random.choice(OBJECTS),
            random.choice(SUFFIXES + ["", f"duration={random_duration()}"])
        ]
        return " ".join(filter(None, parts))
    elif style < 0.70:
        code = random.choices(
            ["200", "201", "400", "401", "403", "404", "429", "500", "503"],
            weights=[40, 10, 8, 12, 13, 7, 9, 6, 5], k=1
        )[0]
        return (
            f"request method={random.choice(['GET','POST','PUT'])} "
            f"path=/api/v1/{random.choice(['tokens','sessions','audit'])} "
            f"status={code} latency={random_duration()}"
        )
    else:
        return (
            f"{random.choice(ACTION_VERBS)} failed → "
            f"{random.choice(ERROR_PATTERNS)} "
            f"trace={''.join(random.choices('0123456789abcdef', k=16))}"
        )

# ────────────────────────────────────────────────
# MAIN LOOP
# ────────────────────────────────────────────────
def main():
    print("\n" * 2)
    print("═" * 84)
    print(" FAKE LOGS + SCI-FI LOADING BAR  (Ctrl+C to stop)")
    print("═" * 84)
    print()

    line_count = 0
    try:
        while True:
            if line_count > 5 and random.random() < 0.10:
                print_fake_loading_bar()
                line_count = 0
                time.sleep(random.uniform(0.4, 1.4))
                continue

            level = random.choice(LOG_LEVELS)
            if level in ("ERROR", "CRITICAL") and random.random() > 0.25:
                level = random.choice(["INFO", "WARN", "DEBUG"])

            host = random.choice(HOSTS)
            service = random.choice(SERVICES)
            msg = build_message()

            extra = ""
            if random.random() < 0.08:
                extra = f"\n ↳ {random.choice(ERROR_PATTERNS + ['stack trace truncated', 'cause=timeout'])}"

            line = (
                f"{DIM}{random_timestamp()}{RESET} "
                f"{COLORS.get(level, '')}{level:8}{RESET} "
                f"{DIM}{host:18}{RESET} "
                f"{DIM}{service:20}{RESET} "
                f"{msg}{extra}"
            )
            print(line)
            line_count += 1
            time.sleep(random.uniform(0.05, 0.68))

    except KeyboardInterrupt:
        print("\n\nStopped.\n")

if __name__ == "__main__":
    main()
