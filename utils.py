from datetime import timedelta 

def strfdelta(delt):
    """Converts delta to format hours:minutes:seconds"""
    hours, remainder = divmod(delt.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

def time_str_to_timedelta(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)
