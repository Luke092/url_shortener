from unit_of_work import UoW


def get_url_by_id(identifier):
    with UoW() as uow:
        url_repo = uow.get_url_repository()
        url = url_repo.get_by_short_code(identifier)

        if url is None:
            return None

        return {
            'url': url['url'],
            'url_short': url['url_short']
        }
