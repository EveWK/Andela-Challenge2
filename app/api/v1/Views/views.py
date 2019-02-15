from flask import Blueprint, request, make_response, jsonify
from app.api.v1.models.model import Party, parties

parties = Blueprint('parties', __name__)


class PartiesResource:

    @parties.route('/parties', methods=['POST'])
    def post():
        data = request.get_json(force=True)

        name = data['name']
        hqaddress = data['hqaddress']
        logoUrl = data['logoUrl']

        res = Party().save(name, hqaddress, logoUrl)
        return make_response(jsonify({
            "message": "created successfully"
        }))

    @parties.route('/parties', methods=['GET'])
    def get():

        parties = Party().get_all_parties()

        return make_response(jsonify({
            "message": "retrieved successfully",
            "parties": parties
        }))

    @parties.route('/parties', methods=['DELETE'])
    def delete ():
        '''Method for deleting a user'''

        parties = Party().delete(name= "")

        return make_response(jsonify({
                "message": "successfully deleted",
                "parties": parties
            }))

    # @parties.route('/parties', methods=['GET'])
    # def get():
    #
    #     parties = Party().get_party_by_names()
    #
    #     return make_response(jsonify({
    #         "message": "retrieved successfully",
    #         "parties": parties
    #     }))
