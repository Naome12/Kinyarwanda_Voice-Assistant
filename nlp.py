import difflib

qa = {
    "Rwanda Coding Academy iherereye he?": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "Umurwa mukuru w’u Rwanda ni uwuhe?": "Ni Kigali.",
    "Ni bande bayobora u Rwanda?": "Perezida ni Paul Kagame.",
    "Ikirere cy’uyu munsi kimeze gite?": "Ndababarira, sinshobora kureba ikirere ubu.",
    "Ufite imyaka ingahe?": "Ndi porogaramu, nta myaka ngira."
}

def match_question(user_input):
    match = difflib.get_close_matches(user_input, qa.keys(), n=1, cutoff=0.5)
    return qa[match[0]] if match else "Mbabarira, sinasobanukiwe neza icyo ushaka."
