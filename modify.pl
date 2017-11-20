print "Date, Open, Close, High, Low, Volume, Adj Close \n";
while (<>) {
	chop($_);
	print $_;
}
