#!/usr/bin/perl
use strict;
use warnings;
use Cwd;
use File::Path qw/rmtree/;

my $app_dir = shift or usage();
unless (-d $app_dir) {
    die "No such directory: $app_dir\n";
}
my $dev_dir = getcwd();

print "$app_dir => $dev_dir\n";

my @files = glob("$app_dir/*");
for my $f (@files) {
    (my $basename = $f) =~ s#.+/##;
    my $dev_file = "$dev_dir/$basename";
    next unless -e $dev_file;
    
    my $backup = "$f.orig";
    if (! -e $backup) {
        rename $f => $backup or die "Can't rename $f => $backup: $!";
    }
    print "Symlinking $basename\n";
    unlink $f;
    symlink "$dev_dir/$basename" => $f or die "Can't symlink $dev_dir/$basename => $f: $!";
}

exit;

sub usage {
    die <<EOT;
USAGE: $0 <activity directory>

This tool creates symlinks from the Activity directory into the current
working directory.  Any file or directory found in the Activity directory
will be symlinked to the local directory, if it exists.

EOT
}
