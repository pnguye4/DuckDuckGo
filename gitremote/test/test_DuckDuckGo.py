import pytest
from DuckDuckGo import presidents


@pytest.mark.parametrize("last_names", [
    'Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe',
    'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler',
    'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan',
    'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield',
    'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley',
    'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge',
    'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy',
    'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan',
    'Bush', 'Clinton', 'Bush', 'Obama', 'Trump'
])
def test_presidents(last_names):
    found = False
    for p in presidents():
        if last_names in p:
            found = True
    assert found == True


@pytest.mark.parametrize("fakes", ["Nguyen", "Hoang", "Tran", "Spongebob"])
def test_fake_presidents(fakes):
    found = False
    for p in presidents():
        if fakes not in p:
            found = True
    assert found == True

