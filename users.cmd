for /f "tokens=* skip=1" %%a in ('wmic UserAccount get Name') do (
    if not "%%a"=="" (
        :: %%a is a variable containing an account name
    )
)
