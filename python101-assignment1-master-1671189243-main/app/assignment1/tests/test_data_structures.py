from data_structures import min_max_value, replace_special_characters, extend_list, sort_tuples, calculate_number_of_days, update_sets

class TestDataStructures:
    def test_min_max_value(self):
        actual = min_max_value()
        excepted = {'min_key': 'Andrew', 'max_key': 'Sam'}
        assert actual == excepted

    def test_replace_special_characters(self):
        actual = replace_special_characters('/*Jon is @developer & musician!!')
        excepted = "##Jon is #developer # musician##"
        assert actual == excepted


    def test_extend_list(self):
        actual = extend_list()
        excepted = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
        assert actual == excepted

    def test_sort_tuples(self):
        actual = sort_tuples()
        excepted = (('c', 11), ('a', 23), ('d', 29), ('b', 37))
        assert actual == excepted

    def test_calculate_number_of_days(self):
        actual = calculate_number_of_days()
        excepted = 854
        assert actual == excepted

    def test_update_sets(self):
        actual = update_sets()
        excepted = {10, 20, 30, 40, 50, 60, 70}
        assert actual == excepted