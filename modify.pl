print "Date, Open, High, Low, Close, Volume, Adj Close \n";
while (<>) {
	chop($_);
	print $_;
}
