import requests

from .base import Resource


class Users(Resource):
    """
    An interface for interacting with the NewRelic user API.
    """
    def list(self, filter_email=None, filter_ids=None, page=None):
        """
        This API endpoint returns a paginated list of the Users
        associated with your New Relic account. Users can be filtered
        by their email or by a list of user IDs.

        :type filter_email: str
        :param filter_email: Filter by user email

        :type filter_ids: list of ints
        :param filter_ids: Filter by user ids

        :type page: int
        :param page: Pagination index

        :rtype: dict
        :return: The JSON response of the API
        """
        filters = [
            'filter[email]={0}'.format(filter_email) if filter_email else None,
            'filter[ids]={0}'.format(','.join([str(app_id) for app_id in filter_ids])) if filter_ids else None,
            'page={0}'.format(page) if page else None
        ]

        response = requests.get(
            url='{0}users.json'.format(self.URL),
            headers=self.headers,
            params=self.build_param_string(filters)
        )
        return response.json()

    def show(self, id):
        """
        This API endpoint returns a single User, identified its ID.

        :type id: int
        :param id: User ID

        :rtype: dict
        :return: The JSON response of the API
        """
        response = requests.get(
            url='{0}users/{1}.json'.format(self.URL, id),
            headers=self.headers,
        )
        return response.json()
