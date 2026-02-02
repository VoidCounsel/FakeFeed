import time
import random
from datetime import datetime

# ────────────────────────────────────────────────
#  WORD LISTS – regular logs
# ────────────────────────────────────────────────

LOG_LEVELS = ["INFO", "WARN", "ERROR", "DEBUG", "CRITICAL", "TRACE", "NOTICE"]

SERVICES = [
    "auth-gateway", "iam-core", "token-validator", "policy-engine",
    "kubelet", "etcd-watch", "control-plane", "sidecar-proxy",
    "otel-collector", "prom-scraper", "alert-dispatcher", "chaos-agent",
    "vector-agent", "fluent-bit", "filebeat", "metricd", "trivy-scanner",
    "vault-agent", "keycloak-sync", "oidc-broker", "sso-bridge",
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
]

ERROR_PATTERNS = [
    "connection refused", "TLS handshake timeout", "certificate expired",
    "invalid signature", "audience mismatch", "rate limit exceeded",
    "circuit breaker open", "upstream timeout", "out of memory",
    "etcdserver: request timed out"
]

# ────────────────────────────────────────────────
#  LOADING BAR WORD POOL – now combinatorial & much more varied
# ────────────────────────────────────────────────

LOAD_VERBS = [
    "Entangling", "Collapsing", "Calibrating", "Synchronizing", "Decrypting",
    "Re-aligning", "Simulating", "Harvesting", "Warming", "Folding",
    "Initializing", "Purging", "Compressing", "Overclocking", "Refactoring",
    "Uploading", "Tuning", "Stabilizing", "Re-weaving", "Bootstrapping",
    "Resolving", "Fracturing", "Amplifying", "Nullifying", "Transmuting",
    "Vectorizing", "Quantizing", "Rehydrating", "Desaturating", "Hyper-threading",
    "Phase-shifting", "Membrane-stretching", "Flux-inverting", "Lattice-repairing",
    "Singularity-seeding", "Causality-pruning", "Entropy-reversing",
]

LOAD_ADVERBS = [
    "quantum", "tachyonic", "chroniton", "zero-point", "brane-world",
    "11-dimensional", "dark-pool", "neutrino-cooled", "subspace", "recursive",
    "temporal", "Planck-scale", "imaginary-unit", "post-singularity",
    "hyperspace", "exotic-matter", "causal", "probability-thread", "shadow",
    "mirror", "entropic", "non-local", "acausal", "retro-causal", "fractal",
    "holographic", "topological", "chiral", "axionic", "supersymmetric",
]

LOAD_OBJECTS = [
    "key distribution nodes", "waveform of shadow partition", "flux capacitor",
    "field harmonics", "energy signature", "membrane tension",
    "firewall lattice", "telemetry entropy", "hash oracle",
    "protein chains", "singularity bootstrap", "echo artifacts",
    "metadata", "unit cache", "blockchain of consciousness",
    "soul fragment checksums", "routing tables", "matter containment",
    "probability threads", "observer", "causal knot", "dimensional anchor",
    "vacuum decay bubble", "brane collision", "topological defect",
    "mirror neuron cluster", "entanglement manifold", "wavefunction collapse",
    "false vacuum tunnel", "axion condensate", "graviton condensate",
]

LOAD_SUFFIXES = [
    "", "matrix", "core", "subsystem", "array", "lattice", "field",
    "resonator", "emitter", "injector", "stabilizer", "dampener",
    "collider", "distributor", "replicator", "forge", "vortex", "anchor",
    "conduit", "singularity", "brane", "membrane", "topos", "sheaf",
]

LOAD_EXTRA = [
    "", "in subspace", "via hyperspace", "under quantum load", "at Planck resolution",
    "in mirror universe", "across 11 branes", "through non-local channels",
    "with retrocausal feedback", "using axionic cooling", "in fractal time",
    "against entropy gradient", "beyond event horizon", "inside causal diamond",
]

def generate_loading_task():
    """Generate varied pseudo-scientific loading task strings"""
    parts = []

    # Most common pattern: Adverb + Verb + Object (+ optional suffix/extra)
    if random.random() < 0.65:
        parts.append(random.choice(LOAD_ADVERBS))
        parts.append(random.choice(LOAD_VERBS).lower())
        parts.append(random.choice(LOAD_OBJECTS))
        
        if random.random() < 0.45:
            parts.append(random.choice(LOAD_SUFFIXES))
        if random.random() < 0.35:
            parts.append(random.choice(LOAD_EXTRA))
    
    # Verb-first style
    elif random.random() < 0.20:
        parts.append(random.choice(LOAD_VERBS))
        parts.append(random.choice(LOAD_OBJECTS))
        if random.random() < 0.6:
            parts.append(random.choice(LOAD_SUFFIXES))
    
    # Over-the-top compound style
    else:
        parts.append(random.choice(["Re-", "Hyper-", "Meta-", "Ultra-", "Post-", "Neo-"]))
        parts.append(random.choice(LOAD_VERBS).lower())
        parts.append(random.choice(LOAD_ADVERBS))
        parts.append(random.choice(LOAD_OBJECTS))
    
    # Capitalize first word
    task = " ".join(parts)
    task = task[0].upper() + task[1:]
    
    return task


# ────────────────────────────────────────────────
#  LOADING BAR – same jittery/fast behavior
# ────────────────────────────────────────────────

BAR_STYLES = ["█", "▓", "▒", "░", "▉", "▊", "▋", "▌", "▍", "▎", "▏", "■", "▣", "▦", "▩", "⬛"]

def print_fake_loading_bar():
    task = generate_loading_task()
    width = random.randint(32, 54)
    total_time_target = random.uniform(2.5, 9.0)

    steps = random.randint(16, 34)

    style_char = random.choice(BAR_STYLES)
    empty_char = random.choice([" ", "·", "░", "⋅"])

    print(f"\n  ┌─ {task.ljust(56)} ─┐")

    current_progress = 0.0
    last_rendered = -1

    for i in range(steps):
        remaining = 1.0 - current_progress
        natural_step = remaining * random.uniform(0.06, 0.28)

        if random.random() < 0.20:
            natural_step *= random.uniform(2.8, 8.0)

        if random.random() < 0.38:
            natural_step *= random.uniform(0.04, 0.45)

        current_progress += natural_step
        current_progress = min(1.0, current_progress)

        filled = int(width * current_progress)
        percent = int(current_progress * 100)

        if filled <= last_rendered and i < steps - 1:
            time.sleep(random.uniform(0.04, 0.45))
            continue

        bar = style_char * filled + empty_char * (width - filled)
        line = f"  │ {bar} {percent:3}% │"
        print(line, end="\r", flush=True)
        last_rendered = filled

        sleep_base = random.uniform(0.04, 0.65)

        if random.random() < 0.18:
            sleep_base += random.uniform(0.4, 1.8)

        if random.random() < 0.20:
            sleep_base *= random.uniform(0.06, 0.30)

        if current_progress > 0.87:
            if random.random() < 0.50:
                sleep_base *= random.uniform(0.08, 0.45)
            else:
                sleep_base *= random.uniform(1.3, 3.2)

        time.sleep(max(0.02, sleep_base))

    bar = style_char * width
    print(f"  │ {bar} 100% │".ljust(72))
    time.sleep(random.uniform(0.08, 0.4))
    print(f"  └─ {task} complete ─┘\n")


# ────────────────────────────────────────────────
#  LOG HELPERS (unchanged)
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
    print("═" * 84)
    print("   FAKE LOG + FAST & HIGHLY RANDOMIZED PROGRESS BARS   –  Ctrl+C to stop")
    print("═" * 84)
    print()

    line_count = 0

    try:
        while True:
            if line_count > 5 and random.random() < 0.09:
                print_fake_loading_bar()
                line_count = 0
                time.sleep(random.uniform(0.3, 1.3))
                continue

            level = random.choice(LOG_LEVELS)
            if level in ("ERROR", "CRITICAL") and random.random() > 0.22:
                level = random.choice(["INFO", "WARN", "DEBUG"])

            host = random.choice(HOSTS)
            service = random.choice(SERVICES)
            msg = build_message()

            extra = ""
            if random.random() < 0.07:
                extra = f"\n      ↳ {random.choice(ERROR_PATTERNS + ['stack trace truncated', 'cause=timeout', 'details redacted'])}"

            line = f"{random_timestamp()}  {level:8}  {host:18}  {service:20}  {msg}{extra}"

            print(line)
            line_count += 1

            time.sleep(random.uniform(0.04, 0.72))

    except KeyboardInterrupt:
        print("\n\nStopped.\n")


if __name__ == "__main__":
    main()
