=begin
Mi primer programa PERL
=end
=cut

use strict;
use warnings;
print "Ingrese un año: ";
my $year = <STDIN>;
chomp ($year);
if ($year % 4 == 0 && $year % 100 != 0 || $year % 400 == 0) {
    print "El año $year es bisiesto\n";
} else {
    print "El año $year no es bisiesto\n";
}