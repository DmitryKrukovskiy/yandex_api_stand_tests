import sender_stand_request
import data

response = sender_stand_request.post_new_user(data.user_body)
auth_token = response.json()['authToken']


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)


    assert kit_response.status_code == 201

    assert kit_response.json()["name"] == name


def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("g")


def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabc")


def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_create_kit_empty_name_get_success_response():
    negative_assert_symbol("")


def test_create_kit_512_letters_in_name_get_success_response():
    negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcd")


def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")


def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")


def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_symbol(kit_body)


def test_create_kit_intejer_in_name_get_success_response():
    negative_assert_symbol(123)