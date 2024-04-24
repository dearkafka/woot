![woot](https://socialify.git.ci/dearkafka/woot/image?description=1&font=Bitter&logo=https%3A%2F%2Fs3.amazonaws.com%2Fpix.iemoji.com%2Fimages%2Femoji%2Fapple%2Fios-12%2F256%2Fowl.png&name=1&theme=Auto)
# 
Woot is a simple Chatwoot API wrapper for Python.
It provides an easy-to-use interface for interacting with the Chatwoot API, allowing you to perform various actions such as creating, retrieving, updating, and deleting conversations, messages, and more.

Also, if you wonder how to use it for Chatwoot webhook have a look at [woothook](https://github.com/dearkafka/woothook)

## Installation

To install Woot, simply run:

```
pip install git+https://github.com/dearkafka/woot
```

## Usage

To use Woot, you'll first need to import the `Chatwoot` or `AsyncChatwoot` class from the `woot`:

```
from woot import Chatwoot, AsyncChatwoot
```

Next, create an instance of `Chatwoot` or `AsyncChatwoot` by passing your Chatwoot URL and access key:

```
chatwoot = Chatwoot(chatwoot_url="https://your-chatwoot-instance.com", access_key="your-access-key")
```

Or, for the async version:

```
async_chatwoot = AsyncChatwoot(chatwoot_url="https://your-chatwoot-instance.com", access_key="your-access-key")
```

You can then access the various resources and perform actions on them as attributes of the `Chatwoot` or `AsyncChatwoot` instance.

![Example1](https://i.imgur.com/hOH0e6Q.gif)

You can also see details about specific methods, but remember **woot takes keyword arguments only, no positional allowed**

![Example2](https://i.imgur.com/lIDV1kw.gif)



## Resources

Woot provides access to various Chatwoot resources, such as:

- Conversations
- Messages
- Contacts
- Labels
- Teams
- Agents
- And more

To access a resource, use the appropriate attribute of the `Chatwoot` or `AsyncChatwoot` instance:

```
conversations = chatwoot.conversations
```

Each resource has a set of actions that can be performed, such as `list`, `create`, `update`, and `delete`. To perform an action, simply call the corresponding method on the resource:

```
all_conversations = conversations.list(account_id=1)
```

## API Documentation

To view the available actions and their corresponding API endpoints for each resource, simply print the `Chatwoot` or `AsyncChatwoot` instance:

```
print(chatwoot)
```

This will display a list of available actions, their HTTP methods, and API endpoints.

## Example

Here's an example demonstrating how to use Woot to list all conversations:

```
from woot import Chatwoot

chatwoot_url = "https://your-chatwoot-instance.com"
access_key = "your-access-key"

chatwoot = Chatwoot(chatwoot_url=chatwoot_url, access_key=access_key)

conversations = chatwoot.conversations
all_conversations = conversations.list(account_id=1)

print(all_conversations)
```

Project is influenced by and borrowed from [simple_rest_client](https://github.com/allisson/python-simple-rest-client) and in fact started by using it as it is, but then I decided to make it more Chatwoot specific and add some features that I needed.


## License
The project is licensed under the Cooperative Non-Violent Public License v7 or later (CNPLv7+) - see the [LICENSE](LICENSE) for details. Built for people, not corporations.
