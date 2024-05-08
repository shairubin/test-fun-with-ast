

LINTER_CODE = "BAZEL_LINTER"
SHA256_REGEX = re.compile(r"\s*sha256\s*=\s*['\"](?P<sha256>[a-zA-Z0-9]{64})['\"]\s*,")
DOMAINS_WITH_UNSTABLE_CHECKSUM = {"github.com"}
