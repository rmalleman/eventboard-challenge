import argparse
from datetime import datetime


def condense_meeting_times_unix_timestamp(meeting_times):
    """
    condense_meeting_times just uses simple boolean conditionals so any data structure that can be compared using
    those operators can be passed to it.  UNIX timestamps meet this criteria so i'm
    just passing it to that function

    :param meeting_times: list of tuples representing meeeting times.
        Example: [('2010-05-08T00:41:54.000000Z', '2010-05-08T01:41:54.000000Z')]
    """
    return condense_meeting_times(meeting_times)


def condense_meeting_times_iso8601(meeting_times):
    """
    for the same reason as with the unix timestamps we can use the condense_meeting_times function but we need
    to convert the strings to datetimes first

    :param meeting_times: list of tuples representing meeeting times.  Example: [(0,1), (4,5)]
    """
    output = []
    for start, end in meeting_times:
        output.append((iso8601_to_datetime(start), iso8601_to_datetime(end)))
    meeting_times_condensed = condense_meeting_times(output)

    output = []
    for start, end in meeting_times_condensed:
        output.append((datetime_to_iso8601(start), datetime_to_iso8601(end)))

    return output


def condense_meeting_times(meeting_times):
    """
    takes in a list of tuples representing meetings and outputs the meeting times in a condensed form

    :param meeting_times: list of tuples representing meeeting times.  Example [(0,1), (4,5)]
    """

    assert(len(meeting_times) > 0)
    output = []
    meeting_times.sort()
    low_time, high_time = meeting_times[0]
    for current_low, current_high in meeting_times[1:]:
        if high_time >= current_low:
            high_time = max(high_time, current_high)
        else:
            output.append((low_time, high_time))
            low_time, high_time = current_low, current_high
    output.append((low_time, high_time))
    return output


def iso8601_to_datetime(datestring):
    """
    iso8601_to_datetime - convert the iso8601 date into a datetime object
    """
    return datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S.%fZ")


def datetime_to_iso8601(date_time):
    """
    converts a datetime to an is8601 string
    """
    return date_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def meeting(s):
    """
    this is just a type for argparse
    """
    try:
        x, y = map(int, s.split(','))
        return x, y
    except:
        raise argparse.ArgumentTypeError("meetings must be x,y")


def meeting_string(s):
    """
    this is just a type for argparse
    """
    try:
        x, y = map(str, s.split(','))
        return x, y
    except:
        raise argparse.ArgumentTypeError("meetings must be x,y")


def main():
    parser = argparse.ArgumentParser(description='Utility to condense meetings')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--meeting', dest='meeting', help="delimit meeting times with a comma (Example: 2,3 4,5 1,2).  "
                                                         "Also works with Unix timestamps",
                        type=meeting, nargs='+')
    group.add_argument('--string_meeting', help="for use with iso8601 formatted strings.  Delimit meeting times with a \
                                                 comma (Example: --string_meeting 2010-05-08T00:41:54.000000Z,2010-05-08T01:41:54.000000Z\
                                                 2010-05-08T02:41:54.000000Z,2010-05-08T05:41:54.000000Z)",
                       type=meeting_string, nargs='+')
    args = parser.parse_args()

    if args.meeting:
        print(condense_meeting_times(args.meeting))
    elif args.string_meeting:
        print(condense_meeting_times_iso8601(args.string_meeting))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()