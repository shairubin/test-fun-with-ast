
def main() -> None:

    job_link = f"[job]({run_url})" if run_url is not None else "job"

    msg = (
        f"The {args.action} {job_link} was canceled. If "
        #+ f" then you can re trigger it through [pytorch-bot]({BOT_COMMANDS_WIKI})."
    )

