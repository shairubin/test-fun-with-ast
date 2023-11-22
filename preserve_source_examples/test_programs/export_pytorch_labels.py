#!/usr/bin/env python3

def main() -> None:
    args = parse_args()
    print(f"Exporting labels for {args.org}/{args.repo}")
    labels_file_name = "pytorch_labels.json"
    obj = boto3.resource("s3").Object("ossci-metrics", labels_file_name)
    obj.put(Body=json.dumps(gh_get_labels(args.org, args.repo)).encode())

