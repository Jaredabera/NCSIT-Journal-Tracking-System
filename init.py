import csv

"""Initialize booked_journals, published_journals"""

file = open("booked_journals.csv", 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Journal Name", "Publish Date", "Publisher Type", "Date of Booking", "Duration", "Expiry Date"])

file = open("published_journals.csv", 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Journal Name", "Publish Date", "Publisher Type"])

file = open("arrived_journals.csv", 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Journal Name", "Arrival Date"])
