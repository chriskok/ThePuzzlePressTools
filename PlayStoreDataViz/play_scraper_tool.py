import play_scraper
import my_list
import csv
import collections
import datetime

# print(play_scraper.suggestions('puzzle'))
# print(my_list.CATEGORIES.keys())

def convert(data):
    if isinstance(data, basestring):
        return data.encode('utf-8').strip()
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def scrape_and_save(collection, category=None, results=120):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = "{}-{}-{}".format(date, collection, category)

    print("creating: {}".format(filename))

    scraped_array = play_scraper.collection(
            collection=collection,
            category=category,
            results=results,
            page=0)

    # for page in range (1,5):
    #     print(page)
    #     scraped_array.extend(play_scraper.collection(
    #             collection='TOP_FREE',
    #             category='GAME_PUZZLE',
    #             results=120,
    #             page=page))

    app_ids = []
    for item in scraped_array:
        app_ids.append(item["app_id"])
        
    app_ids = list(dict.fromkeys(app_ids))

    app_details = []
    for identification in app_ids:
        scraped_details = play_scraper.details(identification)
        if "developer_address" in scraped_details:
            del scraped_details["developer_address"]
        app_details.append(scraped_details)

    app_details = convert(app_details)

    csv_columns = app_details[0].keys()

    csv_file = "GAME_PUZZLE.csv"
    try:
        with open(csv_file, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in app_details:
                writer.writerow(data)
    except IOError:
        print("I/O error") 

def main():
    scrape_and_save('TOP_FREE', category='GAME_PUZZLE', results=10)

if __name__ == '__main__':
    main()