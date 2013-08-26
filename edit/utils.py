import datetime
import jwt
import sys
from peer_edit.settings import ANNOTATE_KEY, ANNOTATE_SECRET
from django.http import HttpResponse

# Replace these with your details
CONSUMER_KEY = ANNOTATE_KEY
CONSUMER_SECRET = ANNOTATE_SECRET

# Only change this if you're sure you know what you're doing
CONSUMER_TTL = 86400

def generate_token(request, paper_id):
	data=jwt.encode({
		'consumerKey': CONSUMER_KEY,
		'userId': request.user.username,
		'paperId': paper_id,
		'issuedAt': _now().isoformat() + 'Z',
		'ttl': CONSUMER_TTL
	}, CONSUMER_SECRET)
	return HttpResponse(data, mimetype='application/json')


def _now():
    return datetime.datetime.utcnow().replace(microsecond=0)
