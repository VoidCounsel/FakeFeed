import time
import random
from datetime import datetime

# ────────────────────────────────────────────────
#  WORD LISTS
# ────────────────────────────────────────────────

LOG_LEVELS = ["INFO", "WARN", "ERROR", "DEBUG", "CRITICAL", "TRACE", "NOTICE"]

SERVICES = [
    "auth-gateway", "iam-core", "token-validator", "policy-engine",
    "kubelet", "etcd-watch", "control-plane", "sidecar-proxy",
    "otel-collector", "prom-scraper", "alert-dispatcher", "chaos-agent",
    "vector-agent", "fluent-bit", "filebeat", "metricd", "trivy-scanner",
    "vault-agent", "keycloak-sync", "oidc-broker", "sso-bridge",
    "redis-connector", "kafka-producer", "pulsar-client", "nats-jetstream",
    "temporal-worker", "dapr-sidecar", "linkerd-proxy", "istio-citadel",
]

HOSTS = [
    "node-07a", "k8s-worker-42", "ip-172-31-94-112", "ec2-i-0f8d3e2a1b9c4d5e",
    "rke2-master-3", "aks-agentpool-12457890-vmss00000p", "pod-ip-10-244-3-189",
    "gke-g1-small-xyz-789f", "minikube", "kind-control-plane", "talos-ctrl-01"
]

ACTION_VERBS = [
    "processing", "validating", "rejecting", "authorizing", "refreshing",
    "syncing", "reconciling", "evicting", "terminating", "scaling",
    "restarting", "rolling", "draining", "cordon", "uncordon",
    "retrying", "failing", "timeout", "ratelimiting", "throttling",
]

OBJECTS = [
    "JWT", "access-token", "refresh-token", "OIDC-id-token", "SAML-assertion",
    "pod", "deployment", "statefulset", "daemonset", "node", "namespace",
    "secret", "configmap", "ingress", "service", "pvc", "pv",
]

SUFFIXES = [
    "succeeded", "failed", "timed-out", "denied", "accepted", "completed",
    "dropped", "queued", "dequeued", "retried (3)", "status=200", "status=429",
    "http/2", "grpc-code=UNAVAILABLE", "principal=system:serviceaccount:prod:api-rw"
]

ERROR_PATTERNS = [
    "connection refused", "TLS handshake timeout", "certificate expired",
    "invalid signature", "audience mismatch", "rate limit exceeded",
    "circuit breaker open", "upstream timeout", "out of memory",
    "etcdserver: request timed out"
]

# ────────────────────────────────────────────────
#  FAKE LOADING BAR NONSENSE
# ────────────────────────────────────────────────

LOADING_TASKS = [
    "Entangling quantum key distribution nodes",
    "Collapsing waveform of shadow partition",
    "Calibrating tachyonic flux capacitor",
    "Synchronizing chroniton field harmonics",
    "Decrypting zero-point energy signature",
    "Re-aligning brane-world membrane tension",
    "Simulating 11-dimensional firewall lattice",
    "Harvesting dark-pool telemetry entropy",
    "Warming up neutrino-cooled hash oracle",
    "Folding protein chains in subspace",
    "Initializing recursive singularity bootstrap",
    "Purging temporal echo artifacts",
    "Compressing Planck-scale metadata",
    "Overclocking imaginary unit cache",
    "Refactoring blockchain of consciousness",
    "Uploading soul fragment checksums",
    "Tuning hyperspace routing tables",
    "Stabilizing exotic matter containment",
]

BAR_STYLES = [
    "█", "▓", "▒", "░", "▉", "▊", "▋", "▌", "▍", "▎", "▏",
    "⬜", "■", "▣", "▤", "▥", "▦", "▧", "▨", "▩", "⬛"
]

def print_fake_loading_bar():
    task = random.choice(LOADING_TASKS)
    width = random.randint(28, 48)
    duration = random.uniform(1.8, 4.8)     # total fake time
    steps = random.randint(18, 36)
    step_time = duration / steps

    style_char = random.choice(BAR_STYLES)
    empty_char = " " if random.random() < 0.7 else random.choice(["·", "-", "░", "⋅"])

    print(f"\n  ┌─ {task.ljust(50)} ─┐")
    
    for i in range(steps + 1):
        progress = i / steps
        filled = int(width * progress)
        bar = style_char * filled + empty_char * (width - filled)
        percent = int(progress * 100)
        line = f"  │ {bar} {percent:3}% │"
        print(line, end="\r", flush=True)
        time.sleep(step_time * random.uniform(0.6, 1.4))

    # Complete
    bar = style_char * width
    print(f"  │ {bar} 100% │".ljust(60))
    print(f"  └─ {task} complete ─┘\n")


# ────────────────────────────────────────────────
#  LOG HELPERS
# ────────────────────────────────────────────────

def random_timestamp():
    now = datetime.utcnow()
    ms = random.randint(0, 999)
    jitter = random.uniform(-1.4, 2.1)
    ts = now.timestamp() + jitter
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%Y-%m-%d %H:%M:%S") + f".{ms:03d}Z"


def random_duration():
    kinds = [
        f"{random.randint(8, 1200)}ms",
        f"{random.uniform(0.4, 5.9):.2f}s",
        f"{random.randint(1, 9)}.{random.randint(0,999):03d}s",
        f"{random.randint(90, 6800)}µs"
    ]
    return random.choice(kinds)


def build_message():
    style = random.random()

    if style < 0.30:
        parts = [
            random.choice(SERVICES),
            random.choice(ACTION_VERBS),
            random.choice(OBJECTS),
            random.choice(SUFFIXES + ["", f"duration={random_duration()}", f"phase={random.choice(['Pending','Running','Terminating','CrashLoopBackOff'])}"])
        ]
        return " ".join(filter(None, parts))

    elif style < 0.55:
        code = random.choices(
            ["200", "201", "204", "400", "401", "403", "404", "429", "500", "502", "503"],
            weights=[38, 9, 11, 7, 10, 12, 6, 8, 5, 3, 4], k=1
        )[0]
        return (
            f"request method={random.choice(['GET','POST','PUT','DELETE'])} "
            f"path=/api/v1/{random.choice(['tokens','sessions','keys','audit','metrics'])} "
            f"status={code} client={random.choice(['10.42.','172.31.','192.168.'])}"
            f"{random.randint(0,255)}.{random.randint(0,255)} "
            f"latency={random_duration()}"
        )

    elif style < 0.80:
        return (
            f"{random.choice(ACTION_VERBS)} failed → "
            f"{random.choice(ERROR_PATTERNS)} "
            f"component={random.choice(SERVICES)} "
            f"trace={''.join(random.choices('0123456789abcdef', k=16))}"
        )

    else:
        fragments = [
            f"[{random.choice(['OK','FAIL','WARN','SKIP','PASS','PENDING'])}]",
            random.choice(SERVICES),
            random.choice(ACTION_VERBS),
            f"0x{random.randint(0, 0xFFFF):04x}",
            f"seq={random.randint(10000,999999999)}",
            f"shard={random.randint(0,31)}",
            f"replica={random.randint(1,5)}/{random.randint(3,7)}"
        ]
        random.shuffle(fragments)
        return " ".join(fragments[:random.randint(3,7)])


# ────────────────────────────────────────────────
#  MAIN LOOP
# ────────────────────────────────────────────────

def main():
    print("\n" * 2)
    print("═" * 80)
    print("   FAKE LOG + PROGRESS-QUEST STYLE LOADING BARS   –  Ctrl+C to stop")
    print("═" * 80)
    print()

    line_count = 0

    try:
        while True:
            # Decide whether to show a fake loading bar
            if line_count > 6 and random.random() < 0.09:  # roughly every 8–25 lines
                print_fake_loading_bar()
                line_count = 0
                time.sleep(random.uniform(0.4, 1.2))
                continue

            level = random.choice(LOG_LEVELS)
            if level in ("ERROR", "CRITICAL") and random.random() > 0.20:
                level = random.choice(["INFO", "WARN", "DEBUG"])

            host = random.choice(HOSTS)
            service = random.choice(SERVICES)
            msg = build_message()

            # occasional multi-line
            extra = ""
            if random.random() < 0.07:
                extra = f"\n      ↳ {random.choice(ERROR_PATTERNS + ['stack trace truncated', 'cause=timeout', 'details redacted'])}"

            line = f"{random_timestamp()}  {level:8}  {host:18}  {service:20}  {msg}{extra}"

            print(line)
            line_count += 1

            time.sleep(random.uniform(0.05, 0.65))

    except KeyboardInterrupt:
        print("\n\nStopped.\n")


if __name__ == "__main__":
    main()
