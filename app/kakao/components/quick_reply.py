from .action import Action
from .extra import Extra

class QuickReply:
    def __init__(self):        
        self.__label = ''
        self.__action = '' # message 혹은 block
        self.__message_text = ''
        self.__block_Id = ''
        self.__extra = ''

    def set_label(self, label : str) -> 'QuickReplies':
        self.__label = label
        return self

    def set_action(self, action : Action) -> 'QuickReplies':
        self.__action = self.__action_navigate(action)
        return self

    def set_message_text(self, message_text : str) -> 'QuickReplies':
        self.__message_text = message_text
        return self

    def set_block_id(self, block_id : str) -> 'QuickReplies':
        self.__block_Id = block_id
        return self
    
    def set_extra(self, extra) -> 'QuickReplies':
        self.__extra = extra
        return self

    def to_string(self) -> str:
        fields = {}
        if self.__label:
            fields["label"] = self.__label
        if self.__action:
            fields["action"] = self.__action
        if self.__message_text:
            fields["messageText"] = self.__message_text
        if self.__block_Id:
            fields["blockId"] = self.__block_Id
        if self.__extra:
            fields["extra"] = self.__extra

        return fields

    def __action_navigate(self, action : Action) -> str: 
        if not isinstance(action, Action):
            raise TypeError('action must be an instance of Action Enum')
        ret = ''        
        if action == Action.MESSAGE:
            ret = "message"        
        elif action == Action.BLOCK:
            ret = "block"
        else:
            raise TypeError('action must be choice MESSAGE or BLOCK  ')
        return ret
