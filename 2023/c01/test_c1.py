from c1 import count_decoder

def test_count_decoder():
    assert count_decoder("hello world hello") == "hello2world1"
    assert count_decoder("a a b c c c") == "a2b1c3"
    assert count_decoder("") == ""
    assert count_decoder("one") == "one1"
    assert count_decoder("one two three four five six seven eight nine ten") == "one1two1three1four1five1six1seven1eight1nine1ten1"

test_count_decoder()
print("Everything passed")