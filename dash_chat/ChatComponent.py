# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ChatComponent(Component):
    """A ChatComponent component.
ChatComponent - A React-based chat interface with customizable styles and typing indicators.
* This component provides a chat interface with support for:
- Displaying messages exchanged between 2 users typically a user and an assistant.
- Customizable themes and styles for the chat UI.
- Typing indicators for both the user and assistant.
- Integration with Dash via the `setProps` callback for state management.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- container_style (dict; optional):
    Inline css styles to customize the chat container.

- fill_height (boolean; default True):
    Whether to vertically fill the screen with the chat container. If
    False, centers and constrains container to a maximum height.

- fill_width (boolean; default True):
    Whether to horizontally fill the screen with the chat container.
    If False, centers and constrains container to a maximum width.

- input_container_style (dict; optional):
    Inline styles for the container holding the message input field.

- input_text_style (dict; optional):
    Inline styles for the message input field itself.

- messages (list of dicts; optional):
    An array of options. The list of chat messages. Each message
    object should have:    - `sender` (string): The message sender,
    either \"user\" or \"assistant\".    - `text` (string): The
    content of the message.

    `messages` is a list of dicts with keys:

    - sender (a value equal to: "user", "assistant"; optional)

    - text (string; required)

- new_message (dict; optional):
    Latest chat message that was appended to messages array.

- theme (string; default "light"):
    Theme for the chat interface. Default is \"light\". Use \"dark\"
    for a dark mode appearance.

- typing_indicator (a value equal to: "dots", "spinner"; default "dots"):
    The type of typing indicator to display. Options are:    -
    `\"dots\"`: Displays animated dots.    - `\"spinner\"`: Displays a
    spinner animation."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_chat'
    _type = 'ChatComponent'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, messages=Component.UNDEFINED, theme=Component.UNDEFINED, container_style=Component.UNDEFINED, typing_indicator=Component.UNDEFINED, new_message=Component.UNDEFINED, input_container_style=Component.UNDEFINED, input_text_style=Component.UNDEFINED, fill_height=Component.UNDEFINED, fill_width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'container_style', 'fill_height', 'fill_width', 'input_container_style', 'input_text_style', 'messages', 'new_message', 'theme', 'typing_indicator']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'container_style', 'fill_height', 'fill_width', 'input_container_style', 'input_text_style', 'messages', 'new_message', 'theme', 'typing_indicator']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChatComponent, self).__init__(**args)
