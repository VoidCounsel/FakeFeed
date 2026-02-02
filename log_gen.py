import time
import random
from datetime import datetime

# ────────────────────────────────────────────────
#  WORD LISTS - feel free to extend them
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
    "envoy-admin", "contour-ingress", "traefik-router", "nginx-ingress",
    "wasm-runtime", "ebpf-sensor", "falco-driver", "sysdig-probe"
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
    "decrypting", "encrypting", "signing", "verifying", "hashing",
    "indexing", "sharding", "rebalancing", "compacting", "snapshotting"
]

OBJECTS = [
    "JWT", "access-token", "refresh-token", "OIDC-id-token", "SAML-assertion",
    "pod", "deployment", "statefulset", "daemonset", "node", "namespace",
    "secret", "configmap", "ingress", "service", "pvc", "pv",
    "rbac-binding", "clusterrole", "mutating-webhook", "crd",
    "span", "trace", "metric", "log-entry", "alert-rule", "silence"
]

SUFFIXES = [
    "succeeded", "failed", "timed-out", "denied", "accepted", "completed",
    "dropped", "queued", "dequeued", "retried (3)", "retried (7)",
    "status=200", "status=401", "status=403", "status=429", "status=502",
    "http/2", "grpc/1.0", "grpc-code=UNAVAILABLE", "grpc-code=DEADLINE_EXCEEDED",
    "client=10.244.2.81", "principal=system:serviceaccount:prod:api-rw"
]

ERROR_PATTERNS = [
    "connection refused", "TLS handshake timeout", "certificate expired",
    "invalid signature", "audience mismatch", "issuer not trusted",
    "rate limit exceeded", "circuit breaker open", "upstream timeout",
    "out of memory", "too many open files", "database unreachable",
    "leader election lost", "lease expired", "etcdserver: request timed out"
]

# ────────────────────────────────────────────────
#  HELPER FUNCTIONS
# ────────────────────────────────────────────────

def random_timestamp():
    # slightly jittered current time (looks more real)
    now = datetime.utcnow()
    ms = random.randint(0, 999)
    jitter_sec = random.uniform(-1.2, 1.8)
    ts = now.timestamp() + jitter_sec
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%Y-%m-%d %H:%M:%S") + f".{ms:03d}Z"


def random_duration():
    # realistic looking durations
    kinds = [
        f"{random.randint(12, 980)}ms",
        f"{random.uniform(0.8, 4.7):.2f}s",
        f"{random.randint(1, 12)}.{random.randint(0,999):03d}s",
        f"{random.randint(200, 4500)}µs"
    ]
    return random.choice(kinds)


def build_message():
    style = random.random()

    if style < 0.35:
        # ── Kubernetes / container style ───────────────
        parts = [
            random.choice(SERVICES),
            random.choice(ACTION_VERBS),
            random.choice(OBJECTS),
            random.choice(SUFFIXES + ["", f"duration={random_duration()}", f"phase={random.choice(['Pending','Running','Terminating'])}"])
        ]
        return " ".join(filter(None, parts))

    elif style < 0.60:
        # ── HTTP / auth / API style ────────────────────
        code = random.choices(
            ["200", "201", "204", "400", "401", "403", "404", "429", "500", "502", "503"],
            weights=[35, 8, 12, 6, 9, 11, 5, 7, 4, 2, 3], k=1
        )[0]

        return (
            f"request completed method={random.choice(['GET','POST','PUT','PATCH','DELETE'])} "
            f"path=/api/v1/{random.choice(['tokens','sessions','users','roles','permissions'])} "
            f"status={code} "
            f"client_ip={random.choice(['10.42.','172.16.','192.168.'])}"
            f"{random.randint(0,255)}.{random.randint(0,255)} "
            f"duration={random_duration()}"
        )

    elif style < 0.80:
        # ── Error / warning style ──────────────────────
        return (
            f"{random.choice(ACTION_VERBS)} failed - "
            f"{random.choice(ERROR_PATTERNS)} "
            f"component={random.choice(SERVICES)} "
            f"trace_id={''.join(random.choices('0123456789abcdef', k=16))}"
        )

    else:
        # ── Generic high-tech noise ────────────────────
        fragments = [
            f"[{random.choice(['OK','FAIL','WARN','SKIP','PASS'])}]",
            random.choice(SERVICES),
            random.choice(ACTION_VERBS),
            f"0x{random.randint(0, 0xFFFF):04x}",
            f"seq={random.randint(100000,999999999)}",
            f"shard={random.randint(0,15)}",
            f"replica={random.randint(1,5)}/{random.randint(3,5)}"
        ]
        random.shuffle(fragments)
        return " ".join(fragments[:random.randint(3,6)])


# ────────────────────────────────────────────────
#  MAIN LOOP
# ────────────────────────────────────────────────

def main():
    print("\n" * 2)
    print("═" * 80)
    print("  FAKE LOG GENERATOR  –  Ctrl+C to stop")
    print("═" * 80)
    print()

    try:
        while True:
            level = random.choice(LOG_LEVELS)
            weight = random.random()

            # make ERROR/CRITICAL less common
            if level in ("ERROR", "CRITICAL") and weight > 0.18:
                level = random.choice(["INFO", "WARN", "DEBUG"])

            host = random.choice(HOSTS)
            service = random.choice(SERVICES)
            msg = build_message()

            # occasional multi-line log entry
            if random.random() < 0.08:
                extra = f"    ↳ {random.choice(ERROR_PATTERNS + ['stack=unknown', 'details omitted', 'cause=timeout'])}"
                msg += "\n" + extra

            line = f"{random_timestamp()}  {level:8}  {host:18}  {service:20}  {msg}"

            print(line)
            time.sleep(random.uniform(0.07, 0.70))   # vary speed a bit

    except KeyboardInterrupt:
        print("\n\nStopped.\n")


if __name__ == "__main__":
    main()
