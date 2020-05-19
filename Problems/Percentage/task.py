def get_percentage(number, round_digits=0):
    percentage = round(number * 100, round_digits)
    return f"{int(percentage) if round_digits == 0 else percentage}%"
