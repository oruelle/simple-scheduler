#!/usr/bin/env python3

import sys
import argparse
from gantt import Chart, Project, Task, Resource

def main():
    # Where we reading from?
    parser = argparse.ArgumentParser(description='Create a Gantt chart from a CSV.')
    parser.add_argument('input', help='''CSV to read data from. CSV must have the headers "Resource",
                                    "Dependency", "Task", and "Duration".''')
    parser.add_argument('-o','--output', help='''Name of SVG file to write to''', default="out.svg")
    args = parser.parse_args()

    # Create resources and tasks from CSV
    chart = Chart(args.input)
    project = Project(args.input)
    chart.add_project(project)

    # Draw
    chart.calculate_schedule()
    print(chart)
    chart.save_svg(args.output)

if __name__ == '__main__':
    sys.exit(main())
