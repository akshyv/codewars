# convert seconds to hh:mm:ss format
# %%
# my solution


def make_readable(seconds):
    if seconds <= 59:
        hour = '00'
        minu = '00'
        s = str(seconds).zfill(2)
        return(f"{hour}:{minu}:{s}")
    else:
        m = seconds//60
        s = seconds % 60
        if m <= 59:
            hour = '00'
            minu = str(m).zfill(2)
            sec = str(s).zfill(2)
            return(f"{hour}:{minu}:{sec}")
        else:
            h = m//60
            m = m % 60
            hour = str(h).zfill(2)
            minu = str(m).zfill(2)
            sec = str(s).zfill(2)
            return(f"{hour}:{minu}:{sec}")
# %%
# sol 1


def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
# %%
# sol 2


def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
# %%
# sol 2


def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)
