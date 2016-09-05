/* based on software 

 Copyright (c) 2008 John Graham-Cumming

 (Released under the BSD License)
 See http://www.grc.com/ppp.htm

*/

// Divide an unsigned 128-bit integer by an unsigned integer and return
// the remainder
char bigdivide(char *big, size_t bytes, unsigned int small, unsigned int *remainder) {
	unsigned int c = 0;
	char nonzero = 0;

	for (size_t i = 0; i < bytes; ++i) {	// big-endian MSB first
		//for (size_t i = bytes-1; i>=0;--i ) {// little-endian LSB first
		unsigned int v = (big[i] & 0xff) + c;
		unsigned int r = v / small;
		c = (v << 8) - ((r << 8) * small);
		big[i] = r & 0xff;
		nonzero |= big[i];
	}
	*remainder = c >> 8;
	return nonzero;
}
