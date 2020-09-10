from django import template


register = template.Library()

@register.filter(name = 'lookup')
def lookup(l, i):
	return l[i]
	
@register.filter(name = 'sub')
def subtract(value, arg):
    return int(value) - arg
	

@register.filter(name = 'filterNames')
def filterNames(d):
	acceptNames = ["BIRTHDAY_SPACINGS_TEST", "BINARY_RANK_TEST_for_31x31_matrices", "BINARY_RANK_TEST_for_32x32_matrices",
	"BINARY_RANK_TEST_for_6x8_matrices", "PARKING_LOT_TEST", "THE_MINIMUM_DISTANCE_TEST", "THE_3DSPHERES_TEST", "SQEEZE_TEST",
	"OVERLAPPING_SUMS_TEST"]
	
	return dict((name, p) for name, p in d.items() if name in acceptNames)
	
	
@register.filter(name = 'filterNames2')
def filterNames2(d):
	acceptNames = ["THE_OVERLAPPING_5_PERMUTATION_TEST", "COUNT_THE_1s_TEST_on_a_stream_of_bytes"]
	return dict((name, p) for name, p in d.items() if name in acceptNames)

@register.filter(name = 'toFloat')	
def toFloat(s):
	return float(s)
	
@register.filter(name = 'toInt')	
def toInt(s):
	return int(s)

