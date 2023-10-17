from ..attribute_processor import AttributeProcessorError
from .base_processor import BaseProcessor
import urllib.parse

CONFIG_KEY_PREFIX = 'prefix'
CONFIG_DEFAULT_PREFIX = ''


class PrefixProcessor(BaseProcessor):   
    def process(self, data, attribute, **kwargs):
        prefix = kwargs.get(CONFIG_KEY_PREFIX, CONFIG_DEFAULT_PREFIX)
        
        if prefix is None or prefix == '':
            raise AttributeProcessorError("No prefix set.")
            
        if prefix == 'issuer_entityid':
            parsed_url = urllib.parse.urlparse(data.auth_info.issuer)
            prefix = parsed_url.scheme + '://' + parsed_url.netloc + '/'

        attributes = data.attributes
        values = attributes.get(attribute, [])
        
        if not isinstance(values, list):
            values = [values]
            
        if values:
            attributes[attribute] = list(prefix + v for v in values)