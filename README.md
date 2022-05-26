# Progressive taxation on the AUD

The main files contained in this repository are:

- `tax.py` module;
- files to build an online article on progressive taxation and bracket creep.'

## Tax module

The module `tax.py` consists of methods:

- `netIncome`, which calculates the income *net* of taxation in Australia's progressive tax system;
- in reverse, `netIncomeInverse` which calculates the *gross* income, given a *net* income;
- `taxPaid`, `taxPaidNet` and `taxPaidGross` which uses the above methods to calculate the tax paid.

## Article

The `gh-pages` branch contains files used to build the article *Bracket Creep*. It is hosted online [here](https://kshkb.github.io/progressive-tax-AUD/bracketcreep.html).

Please see the article for illustrations of the methods in `tax.py`.
