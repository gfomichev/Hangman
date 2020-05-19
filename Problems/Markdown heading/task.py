def heading(phrase, indent=1):
    return f"{'#' * min(max(1, indent), 6)} {phrase}"
