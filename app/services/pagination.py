
def make_pagination(response, page_number, page_size):
    start = (page_number - 1) * page_size
    end = start + page_size
    return response[start:end]