from .models import Client

def authenticate_client(client_id, client_secret=None):
    try:
        client = Client.objects.get(client_id=client_id)

        # For public clients, skip secret validation
        if client.client_type == "confidential" and not client_secret:
            return None

        # For confidential clients, validate secret if provided
        if (
            client.client_type == "confidential"
            and client_secret != client.client_secret
        ):
            return None

        return client
    except Client.DoesNotExist:
        return None


def validate_redirect_uri(client, redirect_uri):
    return redirect_uri in client.redirect_uris.split(",")
