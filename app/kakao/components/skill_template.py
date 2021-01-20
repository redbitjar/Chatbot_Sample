from .component_base import OutputComponent
from .quick_reply import QuickReply


class SkillTemplate:
    def __init__(self):
        self.__version = "2.0"
        self.__outputs = []
        self.__quick_replies = []

    def set_add_output(self, output : OutputComponent):
        if(len(self.__outputs) > 3):
            raise ValueError("3개 이하만 가능 합니다")
        else:
            self.__outputs.append(output)
    
    def set_add_quick_reply(self, quick_reply : QuickReply):
        if(len(self.__quick_replies) > 10):
            raise ValueError("10개 이하만 가능 합니다")        
        else:
            self.__quick_replies.append(quick_reply)


    def to_string(self) -> str:
        fields = {
            "version" : self.__version,
            "template": {
                "outputs":[]
            }
        }
        for o in self.__outputs:
            fields['template']['outputs'].append(o.to_string())
        
        if not fields['template'].get('quickReplies'):
            fields['template']['quickReplies'] = []
        
        for q in self.__quick_replies:
            fields['template']['quickReplies'].append(q.to_string())

        return fields
