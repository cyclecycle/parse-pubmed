import re


def element_text(el):
    text = ''
    if el.tag == 'title':
        try:
            return el.text + '. '
        except:
            return text
    try: text += el.text
    except: pass
    try: text += el.tail
    except: pass
    return text


def all_element_content(el, join=False):
    content = [element_text(child) for child in el.iter()]
    if join:
        content = ''.join(content)
        re.sub(r'\n', '. ', content)
        content = ' '.join(content.split())
        re.sub(r'\.{2,}', '. ', content)
        return content
    content = [' '.join(s.split()) for s in content]
    content = [s for s in content if s]
    return content