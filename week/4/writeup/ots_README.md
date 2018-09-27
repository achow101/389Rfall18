# OpenTimestamps Proofs

The `*.ots` files in this folder are [OpenTimestamps](https://opentimestamps.org/) proofs that the files they are named after existed on or before a particular date.
These proofs commit the hashes of those files to the Bitcoin blockchain thereby providing a proof that the file existed at least at the time the block containing the transaction that contains the hash was mined.
I have included these proofs for when I inevitably forget to merge a homework branch with the master branch and thus miss the time when the script pulls down all of the homeworks.
These will prove that I completed the homework before the due date but messed up the submission process.

## Verifying

To verify these proofs, you will need to install the [OpenTimestamps client](https://github.com/opentimestamps/opentimestamps-client).
You will also need access to a Bitcoin node.
By default it uses a local node, however remote ones can be used as well so long as their URLs (of the form `http://<username>:<password>@<ip address>:<port>`) are known.
Once it is installed use the `ots verify` command for each `.ots` file.

For example, to verify the timestamp for `README.md`, you do:

    ots verify README.md.ots

To specify a particular remote node, you do:

    ots --bitcoin-node http://<username>:<password>@<ip address>:<port> verify README.md.ots
