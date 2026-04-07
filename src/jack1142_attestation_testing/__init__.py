import sys

from pypi_attestations import Attestation
from sigstore.models import Bundle


def main() -> None:
    bundle_file = sys.argv[1]
    with open(bundle_file, "rb") as fp:
        sigstore_bundle = Bundle.from_json(fp.read())
    attestation = Attestation.from_bundle(sigstore_bundle)
    for filename in sys.argv[2:]:
        with open(f"{filename}.build.attestation", "w") as fp:
            fp.write(attestation.model_dump_json())
