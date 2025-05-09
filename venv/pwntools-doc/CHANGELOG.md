# Changelog

This changelog only includes added major features and changes. Bugfixes and
minor changes are omitted.

## Release History

The table below shows which release corresponds to each branch, and what date the version was released.

| Version          | Branch   | Release Date           |
| ---------------- | -------- | ---------------------- |
| [5.0.0](#500-dev)  | `dev`    |
| [4.15.0](#4150-beta)  | `beta`   |
| [4.14.0](#4141-stable)  | `stable` | Mar 24, 2025
| [4.14.0](#4140)  |          | Jan 15, 2025
| [4.13.1](#4131)  |          | Sep 29, 2024
| [4.13.0](#4130)  |          | Aug 12, 2024
| [4.12.0](#4120)  |          | Feb 22, 2024
| [4.11.1](#4111)  |          | Nov 14, 2023
| [4.11.0](#4110)  |          | Sep 15, 2023
| [4.10.0](#4100)  |          | May 21, 2023
| [4.9.0](#490)    |          | Dec 29, 2022
| [4.8.0](#480)    |          | Apr 21, 2022
| [4.7.1](#471)    |          | Apr 20, 2022
| [4.7.0](#470)    |          | Nov 15, 2021
| [4.6.0](#460)    |          | Jul 12, 2021
| [4.5.1](#451)    |          | May 30, 2021
| [4.5.0](#450)    |          | Apr 30, 2021
| [4.4.0](#440)    |          | Mar 29, 2021
| [4.3.1](#431)    |          | Nov 29, 2020
| [4.3.0](#430)    |          | Oct 20, 2020
| [4.2.0](#420)    |          | Jul 3, 2020
| [4.1.7](#417)    |          | Jun 30, 2020
| [4.1.5](#415)    |          | Jun 27, 2020
| [4.1.4](#414)    |          | Jun 26, 2020
| [4.1.3](#413)    |          | Jun 23, 2020
| [4.1.2](#412)    |          | Jun 5, 2020
| [4.1.1](#411)    |          | Jun 3, 2020
| [4.1.0](#410)    |          | May 8, 2020
| [4.0.1](#401)    |          | Jan 22, 2020
| [4.0.0](#400)    |          | Jan 09, 2020
| [3.13.0](#3130)  |          | Nov 5, 2019
| [3.12.2](#3122)  |          | Jan 8, 2019
| [3.12.1](#3121)  |          | Sept 17, 2018
| [3.12.0](#3120)  |          | Feb 22, 2018
| [3.11.0](#3110)  |          | Jan 3, 2018
| [3.10.0](#3100)  |          | Oct 25, 2017
| [3.9.2](#392)    |          | Oct 5, 2017
| [3.9.1](#391)    |          | Sep 28, 2017
| [3.9.0](#390)    |          | Sep 11, 2017
| [3.8.0](#380)    |          | Jul 29, 2017
| [3.7.1](#371)    |          | Jul 14, 2017
| [3.7.0](#370)    |          | Jun 19, 2017
| [3.6.1](#361)    |          | May 12, 2017
| [3.6.0](#360)    |          | May 8, 2017
| [3.5.1](#351)    |          | Apr 15, 2017
| [3.5.0](#350)    |          | Mar 26, 2017
| [3.4.1](#341)    |          | Feb 17, 2017
| [3.4.0](#340)    |          | Feb 13, 2017
| [3.3.4](#334)    |          | Jan 12, 2016
| [3.3.3](#333)    |          | Jan 10, 2016
| [3.3.2](#332)    |          | Jan 10, 2016
| [3.3.1](#331)    |          | Jan 10, 2016
| [3.3.0](#330)    |          | Dec 24, 2016
| [3.2.1](#321)    |          | Dec 24, 2016
| [3.2.0](#320)    |          | Nov 12, 2016
| [3.1.1](#311)    |          | Oct 23, 2016
| [3.1.0](#310)    |          | Oct 2, 2016
| [3.0.4](#304)    |          | Sept 19, 2016
| [3.0.3](#303)    |          | Sept 18, 2016
| [3.0.2](#302)    |          | Sept 6, 2016
| [3.0.1](#301)    |          | Aug 20, 2016
| [3.0.0](#300)    |          | Aug 20, 2016
| [2.2.0](#220)    |          | Jan 5, 2015

## 5.0.0 (`dev`)

- [#2551][2551] Detect when kitty is being used as terminal
- [#2519][2519] Drop Python 2.7 support / Require Python 3.10
- [#2507][2507] Add `+LINUX` and `+WINDOWS` doctest options and start proper testing on Windows
- [#2522][2522] Support starting a kitty debugging window with the 'kitten' command
- [#2524][2524] Raise EOFError during `process.recv` when stdout closes on Windows
- [#2526][2526] Properly make use of extra arguments in `packing` utilities. `sign` parameter requires keyword syntax to specify it.
- [#2517][2517] Allow to passthru kwargs on `ssh.__getattr__` convenience function to fix SSH motd problems
- [#2527][2527] Allow setting debugger path via `context.gdb_binary`
- [#2530][2530] Do NOT error when passing directory arguments in `checksec` commandline tool.
- [#2529][2529] Add LoongArch64 support
- [#2506][2506] ROP: fix `ROP(ELF(exe)).leave` is `None` in some ELF
- [#2504][2504] doc: add example case for `tuple` (host, port pair) in `gdb.attach`
- [#2546][2546] ssh: Allow passing disabled_algorithms keyword argument from ssh to paramiko

[2551]: https://github.com/Gallopsled/pwntools/pull/2551
[2519]: https://github.com/Gallopsled/pwntools/pull/2519
[2507]: https://github.com/Gallopsled/pwntools/pull/2507
[2522]: https://github.com/Gallopsled/pwntools/pull/2522
[2524]: https://github.com/Gallopsled/pwntools/pull/2524
[2526]: https://github.com/Gallopsled/pwntools/pull/2526
[2517]: https://github.com/Gallopsled/pwntools/pull/2517
[2527]: https://github.com/Gallopsled/pwntools/pull/2527
[2530]: https://github.com/Gallopsled/pwntools/pull/2530
[2529]: https://github.com/Gallopsled/pwntools/pull/2529
[2506]: https://github.com/Gallopsled/pwntools/pull/2506
[2504]: https://github.com/Gallopsled/pwntools/pull/2504
[2546]: https://github.com/Gallopsled/pwntools/pull/2546

## 4.15.0 (`beta`)

- [#2508][2508] Ignore a warning when compiling with asm on nix
- [#2471][2471] Properly close spawned kitty window
- [#2358][2358] Cache output of `asm()`
- [#2457][2457] Catch exception of non-ELF files in checksec.
- [#2444][2444] Add `ELF.close()` to release resources
- [#2413][2413] libcdb: improve the search speed of `search_by_symbol_offsets` in local libc-database
- [#2470][2470] Fix waiting for gdb under WSL2
- [#2479][2479] Support extracting libraries from Docker image in `pwn template`
- [#2483][2483] Only print `checksec` output of `ELF.libc` when it was printed for the `ELF` already
- [#2482][2482] Throw error when using `sni` and setting `server_hostname` manually in `remote`
- [#2478][2478] libcdb-cli: add `--offline-only`, refactor unstrip and add fetch parser for download libc-database
- [#2484][2484] Allow to disable caching
- [#2291][2291] Fix attaching to a gdbserver with tuple `gdb.attach(('0.0.0.0',12345))`
- [#2410][2410] Add `tube.upload_manually` to upload files in chunks
- [#2502][2502] Fix loading ELF files without valid .dynamic section
- [#2476][2476] Deprecate 'keepends' argument in favor of 'drop' in `tube.recvline*`
- [#2364][2364] Deprecate direct commandline scripts invocation and exclude nonsense ones

[2508]: https://github.com/Gallopsled/pwntools/pull/2508
[2471]: https://github.com/Gallopsled/pwntools/pull/2471
[2358]: https://github.com/Gallopsled/pwntools/pull/2358
[2457]: https://github.com/Gallopsled/pwntools/pull/2457
[2444]: https://github.com/Gallopsled/pwntools/pull/2444
[2413]: https://github.com/Gallopsled/pwntools/pull/2413
[2470]: https://github.com/Gallopsled/pwntools/pull/2470
[2479]: https://github.com/Gallopsled/pwntools/pull/2479
[2483]: https://github.com/Gallopsled/pwntools/pull/2483
[2482]: https://github.com/Gallopsled/pwntools/pull/2482
[2478]: https://github.com/Gallopsled/pwntools/pull/2478
[2484]: https://github.com/Gallopsled/pwntools/pull/2484
[2291]: https://github.com/Gallopsled/pwntools/pull/2291
[2410]: https://github.com/Gallopsled/pwntools/pull/2410
[2502]: https://github.com/Gallopsled/pwntools/pull/2502
[2476]: https://github.com/Gallopsled/pwntools/pull/2476
[2364]: https://github.com/Gallopsled/pwntools/pull/2364

## 4.14.1 (`stable`)

- [#2451][2451] Show symbols defined to value 0 (start of file)
- [#2533][2533] Fix installation on Python 3.5 and lower
- [#2518][2518] fix: update apport coredump path handling for CorefileFinder
- [#2552][2552] Fix memcpy shellcraft template off-by-one
- [#2559][2559] Fix parsing corefile with missing auxv
- [#2562][2562] Fix syntax highlighting of multiline comments in ASM
- [#2565][2565] Exclude broken Unicorn

[2451]: https://github.com/Gallopsled/pwntools/pull/2451
[2533]: https://github.com/Gallopsled/pwntools/pull/2533
[2518]: https://github.com/Gallopsled/pwntools/pull/2518
[2552]: https://github.com/Gallopsled/pwntools/pull/2552
[2559]: https://github.com/Gallopsled/pwntools/pull/2559
[2562]: https://github.com/Gallopsled/pwntools/pull/2562
[2565]: https://github.com/Gallopsled/pwntools/pull/2565

## 4.14.0

- [#2356][2356] Add local libc database provider for libcdb
- [#2360][2360] Add offline parameter for `search_by_hash` series function
- [#2388][2388] libcdb: add `offline_only` to `search_by_symbol_offsets`
- [#2374][2374] libcdb.unstrip_libc: debug symbols are fetched only if not present
- [#2327][2327] Add basic support to debug processes on Windows
- [#2437][2437] Support asm/disasm on Windows
- [#2330][2330] Change `context.newline` when setting `context.os` to `"windows"`
- [#2322][2322] Add basic RISCV64 shellcraft support
- [#2376][2376] Return buffered data on first EOF in tube.readline()
- [#2371][2371] Add functions for retrieving process mappings
- [#2398][2398] Add support for generating multiple shellcodes at a time in shellcraft
- [#2389][2389] Fix passing bytes to `context.log_file` and `crc.BitPolynom`
- [#2391][2391] Fix error message when passing invalid kwargs to `xor`
- [#2387][2387] Convert apport_corefile() output from bytes-like object to string
- [#2415][2415] Add shellcraft template for IPv6 socket
- [#2405][2405] Add "none" ssh authentication method
- [#2427][2427] Document behaviour of remote()'s sni argument as string.
- [#2382][2382] added optional port, gdb_args and gdbserver_args parameters to gdb.debug()
- [#2435][2435] Speed up gdbserver handshake in gdb.debug()
- [#2436][2436] Add resolution_addr parameter to Ret2dlresolvePayload
- [#2497][2497] Fix remote.fromsocket() to handle AF_INET6 socket

[2436]: https://github.com/Gallopsled/pwntools/pull/2436
[2371]: https://github.com/Gallopsled/pwntools/pull/2371
[2360]: https://github.com/Gallopsled/pwntools/pull/2360
[2356]: https://github.com/Gallopsled/pwntools/pull/2356
[2374]: https://github.com/Gallopsled/pwntools/pull/2374
[2327]: https://github.com/Gallopsled/pwntools/pull/2327
[2322]: https://github.com/Gallopsled/pwntools/pull/2322
[2330]: https://github.com/Gallopsled/pwntools/pull/2330
[2389]: https://github.com/Gallopsled/pwntools/pull/2389
[2391]: https://github.com/Gallopsled/pwntools/pull/2391
[2376]: https://github.com/Gallopsled/pwntools/pull/2376
[2387]: https://github.com/Gallopsled/pwntools/pull/2387
[2388]: https://github.com/Gallopsled/pwntools/pull/2388
[2398]: https://github.com/Gallopsled/pwntools/pull/2398
[2415]: https://github.com/Gallopsled/pwntools/pull/2415
[2405]: https://github.com/Gallopsled/pwntools/pull/2405
[2427]: https://github.com/Gallopsled/pwntools/pull/2405
[2382]: https://github.com/Gallopsled/pwntools/pull/2382
[2435]: https://github.com/Gallopsled/pwntools/pull/2435
[2437]: https://github.com/Gallopsled/pwntools/pull/2437
[2497]: https://github.com/Gallopsled/pwntools/pull/2497

## 4.13.1

- [#2445][2445] Fix parsing the PLT on Windows
- [#2466][2466] Fix PLT emulation with Unicorn 2.1.0
- [#2466][2466] Switch to PyPi Simple API for update checks
- [#2467][2467] Fix loading at all on Windows
- [#2469][2469] GDB 15+ rpyc detection

[2445]: https://github.com/Gallopsled/pwntools/pull/2445
[2466]: https://github.com/Gallopsled/pwntools/pull/2466
[2467]: https://github.com/Gallopsled/pwntools/pull/2467
[2469]: https://github.com/Gallopsled/pwntools/pull/2469

## 4.13.0

- [#2242][2242] Term module revamp: activating special handling of terminal only when necessary
- [#2277][2277] elf: Resolve more relocations into GOT entries
- [#2281][2281] FIX: Getting right amount of data for search fix
- [#2293][2293] Add x86 CET status to checksec output
- [#1763][1763] Allow to add to the existing environment in `process` instead of replacing it
- [#2307][2307] Fix `pwn libcdb file` crashing if "/bin/sh" string was not found
- [#2309][2309] Detect challenge binary and libc in `pwn template`
- [#2308][2308] Fix WinExec shellcraft to make sure it's 16 byte aligned
- [#2279][2279] Make `pwn template` always set context.binary
- [#2310][2310] Add support to start a process on Windows
- [#2335][2335] Add lookup optimizations in DynELF
- [#2334][2334] Speed up disasm commandline tool with colored output
- [#2328][2328] Lookup using $PATHEXT file extensions in `which` on Windows
- [#2189][2189] Explicitly define p64/u64 functions for IDE support
- [#2339][2339] Fix: Allow setting attributes on gdb Breakpoints
- [#2323][2323] Retry failed lookups after one week in libcdb
- [#2325][2325] Match against local system libc first in libcdb
- [#2336][2336] Add `ELF.stripped` and `ELF.debuginfo` properties
- [#2161][2161] Add basic support for darwin shellcraft/asm/disasm/run_shellcode/run_assembly
- [#2161][2161] Fix freebsd amd64 SyscallABI
- [#2160][2161] Fix invalid shellcraft.mov on arm64
- [#2284][2161] Fix invalid shellcraft.pushstr_array on arm64
- [#2345][2345] Fix pwn constgrep when it matches a non-constant type
- [#2338][2338] Fix: follow symlink for libs on ssh connection
- [#2341][2341] Launch GDB correctly in iTerm on Mac
- [#2268][2268] Add a `flatten` argument to `ssh.libs`
- [#2347][2347] Fix/workaround Unicorn Engine 1GB limit that calls exit()
- [#2233][2233] Fix gdb.debug: exe parameter now respected, allow empty argv
- [#2373][2373] Fix displaying bright color variation in terminal output
- [#2378][2378] Don't go though a shell in `gdb.debug`

[2242]: https://github.com/Gallopsled/pwntools/pull/2242
[2277]: https://github.com/Gallopsled/pwntools/pull/2277
[2281]: https://github.com/Gallopsled/pwntools/pull/2281
[2293]: https://github.com/Gallopsled/pwntools/pull/2293
[1763]: https://github.com/Gallopsled/pwntools/pull/1763
[2307]: https://github.com/Gallopsled/pwntools/pull/2307
[2309]: https://github.com/Gallopsled/pwntools/pull/2309
[2308]: https://github.com/Gallopsled/pwntools/pull/2308
[2279]: https://github.com/Gallopsled/pwntools/pull/2279
[2310]: https://github.com/Gallopsled/pwntools/pull/2310
[2335]: https://github.com/Gallopsled/pwntools/pull/2335
[2334]: https://github.com/Gallopsled/pwntools/pull/2334
[2328]: https://github.com/Gallopsled/pwntools/pull/2328
[2189]: https://github.com/Gallopsled/pwntools/pull/2189
[2339]: https://github.com/Gallopsled/pwntools/pull/2339
[2323]: https://github.com/Gallopsled/pwntools/pull/2323
[2325]: https://github.com/Gallopsled/pwntools/pull/2325
[2336]: https://github.com/Gallopsled/pwntools/pull/2336
[2161]: https://github.com/Gallopsled/pwntools/pull/2161
[2345]: https://github.com/Gallopsled/pwntools/pull/2345
[2338]: https://github.com/Gallopsled/pwntools/pull/2338
[2341]: https://github.com/Gallopsled/pwntools/pull/2341
[2268]: https://github.com/Gallopsled/pwntools/pull/2268
[2347]: https://github.com/Gallopsled/pwntools/pull/2347
[2233]: https://github.com/Gallopsled/pwntools/pull/2233
[2373]: https://github.com/Gallopsled/pwntools/pull/2373
[2378]: https://github.com/Gallopsled/pwntools/pull/2378

## 4.12.0

- [#2202][2202] Fix `remote` and `listen` in sagemath
- [#2117][2117] Add -p (--prefix) and -s (--separator) arguments to `hex` command
- [#2221][2221] Add shellcraft.sleep template wrapping SYS_nanosleep
- [#2219][2219] Fix passing arguments on the stack in shellcraft syscall template
- [#2212][2212] Add `--libc libc.so` argument to `pwn template` command
- [#2257][2257] Allow creation of custom templates for `pwn template` command
- [#2225][2225] Allow empty argv in ssh.process()
- [#2349][2349] Fix term.readline omitting a trailing \n
- [#2352][2352] add `RETURN_CONST` as an allowed `_const_code` in safeeval

[2202]: https://github.com/Gallopsled/pwntools/pull/2202
[2117]: https://github.com/Gallopsled/pwntools/pull/2117
[2221]: https://github.com/Gallopsled/pwntools/pull/2221
[2219]: https://github.com/Gallopsled/pwntools/pull/2219
[2212]: https://github.com/Gallopsled/pwntools/pull/2212
[2257]: https://github.com/Gallopsled/pwntools/pull/2257
[2225]: https://github.com/Gallopsled/pwntools/pull/2225
[2349]: https://github.com/Gallopsled/pwntools/pull/2349
[2352]: https://github.com/Gallopsled/pwntools/pull/2352

## 4.11.1

- [#2271][2271] FIX: Generated shebang with path to python invalid if path contains spaces
- [#2272][2272] Fix `tube.clean_and_log` not logging buffered data
- [#2281][2281] FIX: Getting right amount of data for search fix
- [#2287][2287] Fix `_countdown_handler` not invoking `timeout_change`
- [#2294][2294] Fix atexit SEGV in aarch64 loader

[2271]: https://github.com/Gallopsled/pwntools/pull/2271
[2272]: https://github.com/Gallopsled/pwntools/pull/2272
[2281]: https://github.com/Gallopsled/pwntools/pull/2281
[2287]: https://github.com/Gallopsled/pwntools/pull/2287
[2294]: https://github.com/Gallopsled/pwntools/pull/2294

## 4.11.0

- [#2185][2185] make fmtstr module able to create payload without $ notation
- [#2103][2103] Add search for libc binary by leaked function addresses `libcdb.search_by_symbol_offsets()`
- [#2177][2177] Support for RISC-V 64-bit architecture
- [#2186][2186] Enhance `ELF.nx` and `ELF.execstack`
- [#2129][2129] Handle `context.newline` correctly when typing in `tube.interactive()`
- [#2214][2214] Fix bug at ssh.py:`download` and `download_file` with relative paths
- [#2241][2241] Fix ssh.process not setting ssh_process.cwd attribute
- [#2261][2261] Fix corefile module after pyelftools update

[2185]: https://github.com/Gallopsled/pwntools/pull/2185
[2103]: https://github.com/Gallopsled/pwntools/pull/2103
[2177]: https://github.com/Gallopsled/pwntools/pull/2177
[2186]: https://github.com/Gallopsled/pwntools/pull/2186
[2129]: https://github.com/Gallopsled/pwntools/pull/2129
[2214]: https://github.com/Gallopsled/pwntools/pull/2214
[2241]: https://github.com/Gallopsled/pwntools/pull/2241
[2261]: https://github.com/Gallopsled/pwntools/pull/2261

## 4.10.0

In memoriam — [Zach Riggle][zach] — long time contributor and maintainer of Pwntools.

- [#2062][2062] make pwn cyclic -l work with entry larger than 4 bytes
- [#2092][2092] shellcraft: dup() is now called dupio() consistently across all supported arches
- [#2093][2093] setresuid() in shellcraft uses current euid by default
- [#2125][2125] Allow tube.recvregex to return capture groups
- [#2144][2144] Removes `p2align 2` `asm()` headers from `x86-32`, `x86-64` and `mips` architectures to avoid inconsistent instruction length when patching binaries

[2062]: https://github.com/Gallopsled/pwntools/pull/2062
[2092]: https://github.com/Gallopsled/pwntools/pull/2092
[2093]: https://github.com/Gallopsled/pwntools/pull/2093
[2125]: https://github.com/Gallopsled/pwntools/pull/2125
[2144]: https://github.com/Gallopsled/pwntools/pull/2144
[zach]: https://github.com/zachriggle

## 4.9.0

- [#1975][1975] Add libcdb commandline tool
- [#1979][1979] Add `js_escape()` and `js_unescape()` to `util.fiddling`
- [#2011][2011] Fix tube's debug output of same byte compression
- [#2023][2023] Support KDE Konsole in run_in_new_terminal function
- [#2027][2027] Fix ELF.libc_start_main_return with glibc 2.34
- [#2033][2033] Quote file and core path in generated GDB script
- [#2035][2035] Change Buffer's parent class to object
- [#2037][2037] Allow SSH tunnel to be treated like a TCP socket (with 'raw=True')
- [#2123][2123] Fix ROP without a writeable cache directory
- [#2124][2124] Fix `tube.recvpred()` timeout argument

[1975]: https://github.com/Gallopsled/pwntools/pull/1975
[1979]: https://github.com/Gallopsled/pwntools/pull/1979
[2011]: https://github.com/Gallopsled/pwntools/pull/2011
[2023]: https://github.com/Gallopsled/pwntools/pull/2023
[2027]: https://github.com/Gallopsled/pwntools/pull/2027
[2033]: https://github.com/Gallopsled/pwntools/pull/2033
[2035]: https://github.com/Gallopsled/pwntools/pull/2035
[2037]: https://github.com/Gallopsled/pwntools/pull/2037
[2123]: https://github.com/Gallopsled/pwntools/pull/2123
[2124]: https://github.com/Gallopsled/pwntools/pull/2124

## 4.8.0

- [#1922][1922] Fix logic in `wait_for_debugger`
- [#1828][1828] libcdb: Load debug info and unstrip libc binary
- [#1939][1939] Fix error in validating log levels
- [#1981][1981] Fix `cyclic_find()` to make it work with large int values

[1922]: https://github.com/Gallopsled/pwntools/pull/1922
[1828]: https://github.com/Gallopsled/pwntools/pull/1828
[1939]: https://github.com/Gallopsled/pwntools/pull/1939
[1981]: https://github.com/Gallopsled/pwntools/pull/1981

## 4.7.1

- [#1784][1784] Use temporary cache directory when persistent cache cannot be used
- [#1973][1973] ELF symbols can be looked up by bytes values
- several bugfixes ([#2012][2012], [#2031][2031], [#1912][1912], [#1961][1961],
[#2007][2007], [#2040][2040], [#2051][2051])

[1784]: https://github.com/Gallopsled/pwntools/pull/1784
[1912]: https://github.com/Gallopsled/pwntools/pull/1912
[1961]: https://github.com/Gallopsled/pwntools/pull/1961
[1973]: https://github.com/Gallopsled/pwntools/pull/1973
[2007]: https://github.com/Gallopsled/pwntools/pull/2007
[2012]: https://github.com/Gallopsled/pwntools/pull/2012
[2031]: https://github.com/Gallopsled/pwntools/pull/2031
[2040]: https://github.com/Gallopsled/pwntools/pull/2040
[2051]: https://github.com/Gallopsled/pwntools/pull/2051

## 4.7.0

- [#1733][1733] Update libc headers -> more syscalls available!
- [#1876][1876] add `self.message` and change `sys.exc_type` to `sys.exec_info()` in PwnlibException
- [#1877][1877] encoders error message handles when `avoid` is bytes in python3
- [#1891][1891] Keep ROP gadgets when setting registers via setattr/call
- [#1892][1892] Silence SIGPIPE error for "pwn phd"
- [#1893][1893] Fix bytes warning in "pwn cyclic"
- [#1897][1897] Add basic support for RISC-V
- [#1903][1903] Add zsh completion script
- [#1904][1904] Add bash completion script
- [#1906][1906] Defer import of several modules to save on startup time
- [#1921][1921] Add basic support for the bare-metal ARM specific toolchain
- [#1995][1995] Add `shellcraft.*.linux.cat2`, which uses alloc+read+write instead of sendfile

[1733]: https://github.com/Gallopsled/pwntools/pull/1733
[1876]: https://github.com/Gallopsled/pwntools/pull/1876
[1877]: https://github.com/Gallopsled/pwntools/pull/1877
[1891]: https://github.com/Gallopsled/pwntools/pull/1891
[1892]: https://github.com/Gallopsled/pwntools/pull/1892
[1893]: https://github.com/Gallopsled/pwntools/pull/1893
[1897]: https://github.com/Gallopsled/pwntools/pull/1897
[1903]: https://github.com/Gallopsled/pwntools/pull/1903
[1904]: https://github.com/Gallopsled/pwntools/pull/1904
[1906]: https://github.com/Gallopsled/pwntools/pull/1906
[1921]: https://github.com/Gallopsled/pwntools/pull/1921
[1995]: https://github.com/Gallopsled/pwntools/pull/1995

## 4.6.0

- [#1429][1429] Add a mechanism for ret2csu (originally #1138)
- [#1566][1566] Add `ignore_config` argument to `pwnlib.tubes.ssh` and improve `allow_agent` implementation
- [#1652][1652] Add `process.readmem` and `process.writemem`
- [#1739][1739] Add/fix shellcraft.linux.kill() / shellcraft.linux.killparent()
- [#1746][1746] Prefer Python3 over Python2 for spawning remote processes over SSH
- [#1751][1751] Fix process() with executable relative to cwd
- [#1753][1753] major change: less unconditional imports in pwnlib
- [#1776][1776] mips: do not use $t0 temporary variable in dupio
- [#1846][1846] support launching GDB in more different terminals

[1429]: https://github.com/Gallopsled/pwntools/pull/1429
[1566]: https://github.com/Gallopsled/pwntools/pull/1566
[1652]: https://github.com/Gallopsled/pwntools/pull/1652
[1739]: https://github.com/Gallopsled/pwntools/pull/1739
[1746]: https://github.com/Gallopsled/pwntools/pull/1746
[1751]: https://github.com/Gallopsled/pwntools/pull/1751
[1753]: https://github.com/Gallopsled/pwntools/pull/1753
[1776]: https://github.com/Gallopsled/pwntools/pull/1776
[1846]: https://github.com/Gallopsled/pwntools/pull/1846

## 4.5.1

- [#1902][1902] Always specify -F and -P for tmux in `run_in_new_terminal`

[1902]: https://github.com/Gallopsled/pwntools/pull/1902

## 4.5.0

- [#1261][1261] Misc `run_in_new_terminal` improvements (notably gdb terminated by default)
- [#1695][1695] Allow using GDB Python API
- [#1735][1735] Python 3.9 support in safeeval
- [#1738][1738] Which function support custom search path
  - process also looks now at `env['PATH']` to find the path for the executable
- [#1742][1742] New `baremetal` os to debug binaries executed with qemu-system-$(arch)
- [#1757][1757] update cache directories
- [#1758][1758] Remove eval from cli
- [#1780][1780] Re-add Python2 to the official Dockerfile
- [#1941][1941] Disable all Android tests, `pwnlib.adb` is no longer supported in CI
- [#1811][1811] Remove unnecessary `pwn.toplevel.__all__`
- [#1827][1827] Support `$XDG_CONFIG_HOME` dir for `pwn.conf`
- [#1841][1841] Add colored_traceback
- [#1839][1839] run_in_new_terminal now creates a runner script if given a list or tuple
- [#1833][1833] Add pwnlib.filesystem module
- [#1852][1852] Fix `atexit` on Python 3
- [#1883][1883] ROP gadget verifier accounts for 2 character registers

[1261]: https://github.com/Gallopsled/pwntools/pull/1261
[1695]: https://github.com/Gallopsled/pwntools/pull/1695
[1735]: https://github.com/Gallopsled/pwntools/pull/1735
[1738]: https://github.com/Gallopsled/pwntools/pull/1738
[1742]: https://github.com/Gallopsled/pwntools/pull/1742
[1757]: https://github.com/Gallopsled/pwntools/pull/1757
[1758]: https://github.com/Gallopsled/pwntools/pull/1758
[1780]: https://github.com/Gallopsled/pwntools/pull/1780
[1941]: https://github.com/Gallopsled/pwntools/pull/1941
[1811]: https://github.com/Gallopsled/pwntools/pull/1811
[1827]: https://github.com/Gallopsled/pwntools/pull/1827
[1841]: https://github.com/Gallopsled/pwntools/pull/1841
[1839]: https://github.com/Gallopsled/pwntools/pull/1839
[1833]:  https://github.com/Gallopsled/pwntools/pull/1833
[1852]: https://github.com/Gallopsled/pwntools/pull/1852
[1883]: https://github.com/Gallopsled/pwntools/pull/1883

## 4.4.0

- [#1541][1541] Use `context.newline` for tubes by default
- [#1602][1602] Fix bytes handling in ssh tubes
- [#1606][1606] Fix `asm()` and `disasm()` for MSP430, S390
- [#1616][1616] Fix `cyclic` cli for 64 bit integers
- [#1632][1632] Enable usage of Pwntools in jupyter
- [#1633][1633] Open a shell if `pwn template` cannot download the remote file
- [#1644][1644] Enable and support SNI for SSL-wrapped tubes
- [#1651][1651] Make `pwn shellcraft` faster
- [#1654][1654] Docker images (`pwntools/pwntools:stable` etc) now use Python3 by default, and includes assemblers for a few common architectures
- [#1667][1667] Add i386 encoder `ascii_shellcode` (Fixed docs in #1693)
- Fix syscall instruction lists for SROP on `i386` and `amd64`
- Fix migration to another ROP
- [#1673][1673] Add `base=` argument to `ROP.chain()` and `ROP.dump()`
- [#1675][1675] Gdbserver now correctly accepts multiple libraries in `LD_PRELOAD` and `LD_LIBRARY_PATH`
- [#1678][1678] ROPGadget multibr
- [#1682][1682] ROPGadget multibr fix
- [#1687][1687] Actually import `requests` when doing `from pwn import *`
- [#1688][1688] Add `__setattr__` and `__call__` interfaces to `ROP` for setting registers
- [#1692][1692] Remove python2 shebangs where appropriate
- [#1703][1703] Update libcdb buildid offsets for amd64 and i386
- [#1704][1704] Try https://libc.rip/ for libcdb lookup

[1541]: https://github.com/Gallopsled/pwntools/pull/1541
[1602]: https://github.com/Gallopsled/pwntools/pull/1602
[1606]: https://github.com/Gallopsled/pwntools/pull/1606
[1616]: https://github.com/Gallopsled/pwntools/pull/1616
[1632]: https://github.com/Gallopsled/pwntools/pull/1632
[1633]: https://github.com/Gallopsled/pwntools/pull/1633
[1644]: https://github.com/Gallopsled/pwntools/pull/1644
[1651]: https://github.com/Gallopsled/pwntools/pull/1651
[1654]: https://github.com/Gallopsled/pwntools/pull/1654
[1667]: https://github.com/Gallopsled/pwntools/pull/1667
[1673]: https://github.com/Gallopsled/pwntools/pull/1673
[1675]: https://github.com/Gallopsled/pwntools/pull/1675
[1678]: https://github.com/Gallopsled/pwntools/pull/1678
[1682]: https://github.com/Gallopsled/pwntools/pull/1679
[1687]: https://github.com/Gallopsled/pwntools/pull/1687
[1688]: https://github.com/Gallopsled/pwntools/pull/1688
[1692]: https://github.com/Gallopsled/pwntools/pull/1692
[1703]: https://github.com/Gallopsled/pwntools/pull/1703
[1704]: https://github.com/Gallopsled/pwntools/pull/1704

## 4.3.1

- [#1732][1732] Fix shellcraft SSTI vulnerability (first major pwntools vuln!)

[1732]: https://github.com/Gallopsled/pwntools/pull/1732

## 4.3.0

- [#1576][1576] Add `executable=` argument to `ELF.search`
- [#1584][1584] Add `jmp_esp`/`jmp_rsp` attribute to `ROP`
- [#1592][1592] Fix over-verbose logging of process() environment
- [#1593][1593] Colorize output of `pwn template`
- [#1601][1601] Add `pwn version` command line tool
- [#1605][1605] Add to `fiddling.hexdump` a way to suppress the total at the end
- [#1613][1613] Permit `--password` for `pwn template`
- [#1616][1616] Fix `cyclic` cli for 64 bit integers
- [#1564][1564] Fix `asm()` and `disasm()` for PowerPC64, MIPS64, Sparc64
- [#1621][1621] Permit negative values in flat() and fit()

[1576]: https://github.com/Gallopsled/pwntools/pull/1576
[1584]: https://github.com/Gallopsled/pwntools/pull/1584
[1592]: https://github.com/Gallopsled/pwntools/pull/1592
[1593]: https://github.com/Gallopsled/pwntools/pull/1593
[1601]: https://github.com/Gallopsled/pwntools/pull/1601
[1605]: https://github.com/Gallopsled/pwntools/pull/1605
[1613]: https://github.com/Gallopsled/pwntools/pull/1613
[1616]: https://github.com/Gallopsled/pwntools/pull/1616
[1564]: https://github.com/Gallopsled/pwntools/pull/1564
[1621]: https://github.com/Gallopsled/pwntools/pull/1621

## 4.2.1

- [#1625][1625] GDB now properly loads executables with QEMU
- [#1663][1663] Change lookup algorithm of `adb.which`
- [#1699][1699] Fix broken linux shellcraft templates

[1625]: https://github.com/Gallopsled/pwntools/pull/1625
[1699]: https://github.com/Gallopsled/pwntools/pull/1699

## 4.2.0

- [#1436][1436] Add ret2dlresolve automation
- [fecf9f] tubes.ssh.process() no longer requires python 2 installed on remote (still requires python, though)
- Miscellanous improvements to DynElf and fmtstr leaker (see examples/fmtstr/exploit2.py)
- [#1454][1454] Support for windows console colors

[1436]: https://github.com/Gallopsled/pwntools/pull/1436
[fecf9f]: http://github.com/Gallopsled/pwntools/commit/fecf9f
[1454]: https://github.com/Gallopsled/pwntools/pull/1454

## 4.1.7 (`stable`)

- [#1615][1615] Fix aarch64 pushstr and pushstr_array

[1615]: https://github.com/Gallopsled/pwntools/pull/1454

## 4.1.5

- [#1517][1517] flat(..., filler=) is fixed for `str` values and Python2 `bytes`

[1517]: https://github.com/Gallopsled/pwntools/pull/1517

## 4.1.4

- [#1698][1609] Fix issues in `packing.flat` with mis-ordred fields

[1609]: https://github.com/Gallopsled/pwntools/pull/1609

## 4.1.3

- [#1590][1590] Fix `gdb.attach()` for `remote`, `listen`, `ssh` tubes
  - Also fix `run_in_new_terminal` for Py2 unicode strings
- [#1595][1595] Fix ssh.process(timeout=)

[1590]: https://github.com/Gallopsled/pwntools/pull/1590
[1595]: https://github.com/Gallopsled/pwntools/pull/1595

## 4.1.2

- Pwntools requires `six` v.1.12.0 or higher

## 4.1.1

- Fix PLT resolution by locking unicorn <1.0.2rc4 (#1538)
- Fix wrong ELF/context unpack handling (c4c11a37)
- Fix updating of ELF.functions addresses after changing ELF.address #1512 (#1513)
- Update Corefile warnings and replace asserts with normal checks (#1526)
- several py2-py3 issues (#1451)
- Fix cyclic command

## 4.1.0

- [#1316][1316] Fix connect shellcraft in python 3
- [#1323][1323] Fix issues related with debugging
- [#1001][1001] Enhance `unlock_bootloader` with better status messages
- [#1389][1389] remove old dependencies
- [#1241][1241] Launch QEMU with sysroot if specified
- [#1218][1218] Support for FileStructure exploitation

[1316]: https://github.com/Gallopsled/pwntools/pull/1316
[1323]: https://github.com/Gallopsled/pwntools/pull/1323
[1001]: https://github.com/Gallopsled/pwntools/pull/1001
[1389]: https://github.com/Gallopsled/pwntools/pull/1389
[1241]: https://github.com/Gallopsled/pwntools/pull/1241
[1218]: https://github.com/Gallopsled/pwntools/pull/1218

## 4.0.1

- [#1412][1412] `recvline_pred()` and similar do not reorder data
- Bypass unicorn-engine/unicorn#1100 and unicorn-engine/unicorn#1170 requiring unstable package

[1412]: https://github.com/Gallopsled/pwntools/pull/1412

## 4.0.0

- **Python 3 support! <3**
- [#1402][1402] Fix serialtube in python 3
- [#1391][1391] Fix process.libs
- [#1317][1317] Tubes with `context.encoding`
- [#1216][1216] Improve format string generator
- [#1285][1285] Add freebsd generic syscall templates
- [76413f][76413f] Add pwnlib.adb.bootimg for 'ANDROID!' format boot.img images
- [#1202][1202] Docker: Kill 14 layers in pwntools base images
- [#1182][1182] shellcraft.dupio() for mips

[1402]: https://github.com/Gallopsled/pwntools/pull/1402
[1391]: https://github.com/Gallopsled/pwntools/pull/1391
[1317]: https://github.com/Gallopsled/pwntools/pull/1317
[1285]: https://github.com/Gallopsled/pwntools/pull/1285
[1216]: https://github.com/Gallopsled/pwntools/pull/1216
[1202]: https://github.com/Gallopsled/pwntools/pull/1202
[1182]: https://github.com/Gallopsled/pwntools/pull/1182
[76413f]: https://github.com/Gallopsled/pwntools/commit/76413f

## 3.13.0

- [#1204][1204] Reduce ROP cache filename length
- [#1175][1175] Fix nested SSH connectors
- [#1355][1355] Fix 'break' syscall
- [#1277][1277] Fix timeout parameter passing in sendlineafter and other similar functions
- [#1292][1292] Provide correct arch name to gdb for sparc64

[1175]: https://github.com/Gallopsled/pwntools/pull/1175
[1204]: https://github.com/Gallopsled/pwntools/pull/1204
[1277]: https://github.com/Gallopsled/pwntools/pull/1277
[1292]: https://github.com/Gallopsled/pwntools/pull/1292
[1355]: https://github.com/Gallopsled/pwntools/pull/1355

## 3.12.2

- [#1242][1242] Use IntervalTree 2.xx, disallow use of 3.xx
- [#1243][1243] Fix a typo that caused an exception when executing a binary with `process()` which returns `-ENOEXEC` and the system does not have `qemu-user` binaries installed.

[1242]: https://github.com/Gallopsled/pwntools/pull/1242
[1243]: https://github.com/Gallopsled/pwntools/pull/1243

## 3.12.1

- [#1198][1198] More compatibility fixes for pyelftools==0.25, and pin Sphinx<1.8.0 since it causes testing errors
- [#1191][1191] Fix compatibility with pyelftools==0.25
- [#1159][1159] Fix check for `/proc/.../status`
- [#1162][1162] Fix broken package versions
- [#1150][1150] Fix exception raised when a cache file is missing
- [#1156][1156] Fix ROP gadget selection logic involving `int` and `syscall` instructions
- [#1152][1152] Fix QEMU LD_PREFIX calculation (wrong parameter passed)
- [#1155][1155] Use Ubuntu Trusty for all CI builds
- [#1131][1131] Add "libc-" to libc prefixes in `process` tubes
- [#1125][1125] Fix a typo
- [#1121][1121] Fix tests which were broken by an upstream Sphinx change
- [#1104][1104] Add `DynELF.dump()` for dumping remote ELF files
- [#1101][1101] Set `context.os` via `context.binary`, useful for Android exploitation
- [5fdc08][5fdc08] Work around broken `pidof` on Android
- [63dfed][63dfed] Print warning when Corefile deletion fails instead of throwing an exception
- [#1094][1094] Make hexdump output alignment more consistent
- [#1096][1096] `flat()` and `fit()` are now the same function

[1198]: https://github.com/Gallopsled/pwntools/pull/1198
[1191]: https://github.com/Gallopsled/pwntools/pull/1191
[1159]: https://github.com/Gallopsled/pwntools/pull/1159
[1162]: https://github.com/Gallopsled/pwntools/pull/1162
[1150]: https://github.com/Gallopsled/pwntools/pull/1150
[1156]: https://github.com/Gallopsled/pwntools/pull/1156
[1152]: https://github.com/Gallopsled/pwntools/pull/1152
[1155]: https://github.com/Gallopsled/pwntools/pull/1155
[1131]: https://github.com/Gallopsled/pwntools/pull/1131
[1125]: https://github.com/Gallopsled/pwntools/pull/1125
[1121]: https://github.com/Gallopsled/pwntools/pull/1121
[1104]: https://github.com/Gallopsled/pwntools/pull/1104
[1101]: https://github.com/Gallopsled/pwntools/pull/1101
[1094]: https://github.com/Gallopsled/pwntools/pull/1094
[1096]: https://github.com/Gallopsled/pwntools/pull/1096
[5fdc08]: https://github.com/Gallopsled/pwntools/commit/5fdc08
[63dfed]: https://github.com/Gallopsled/pwntools/commit/63dfed

## 3.12.0

- [#1083][1083] Better error messages for `gdb` when `LD_PRELOAD` is incorrect
- [#1085][1085] Add support for extracting Android `BOOTLDR!` images
- [#1075][1075] Add support for detecting GNU Screen for `run_in_new_terminal`
- [#1074][1074] Add support for running `pwntools-gdb` wrapper script instead of `gdb`
- [#1068][1068] Work around very old OpenSSL versions which don't have sha256 support *AND* don't exit with an error code when trying to use it
- [#1067][1067] Add `pwnlib.tubes.server` module, which adds a reusable `server` listener
- [#1063][1063] Add support for labels in `fit()`, allowing dynamic contents to be injected.  (This feature is really cool, check out the pull request!)

[1083]: https://github.com/Gallopsled/pwntools/pull/1083
[1085]: https://github.com/Gallopsled/pwntools/pull/1085
[1075]: https://github.com/Gallopsled/pwntools/pull/1075
[1074]: https://github.com/Gallopsled/pwntools/pull/1074
[1068]: https://github.com/Gallopsled/pwntools/pull/1068
[1067]: https://github.com/Gallopsled/pwntools/pull/1067
[1063]: https://github.com/Gallopsled/pwntools/pull/1063

## 3.11.0

- [#1044][1044] Enhancements to ROP
    + Much better support for 64-bit Intel (amd64) ROP
    + ROP gadget selection is optimized to favor multi-pops instead of multiple single-pop gadgets
    + Added support for blacklisting byte values in ROP gadget addresses
- [#1049][1049] Enhancements to `cyclic`
    + `context` now has two additional attributes, `cyclic_alphabet` and `cyclic_length`, which correspond to the arguments `alphabet` and `n` to `cyclic()` and `cyclic_find()` and related routines.
    + The motivation for this change is to allow setting the `alphabet` globally, so that any padding / patterns generated internally to pwntools can be controlled.  The specific motivation is blacklisting values in ROP padding.
- [#1052][1052] Enhancements for detecting `QEMU_LD_PREFIX` used by QEMU user-mode emulation for sysroots
- [#1035][1035] Minor documentation changes
- [#1032][1032] Enhancements to `pwn template`
- [#1031][1031] More accurate `Coredump.fault_addr` on amd64
- [#1084][1084] Fix broken tests due to `ftp.debian.org` going down

[1044]: https://github.com/Gallopsled/pwntools/pull/1044
[1049]: https://github.com/Gallopsled/pwntools/pull/1049
[1052]: https://github.com/Gallopsled/pwntools/pull/1052
[1035]: https://github.com/Gallopsled/pwntools/pull/1035
[1032]: https://github.com/Gallopsled/pwntools/pull/1032
[1031]: https://github.com/Gallopsled/pwntools/pull/1031
[1084]: https://github.com/Gallopsled/pwntools/pull/1084

## 3.10.0

- [#1007][1007] Add support for setting a `gdbinit` file in the context
- [#1055][1055] Fixes for `Corefile` stack parsing, speed up `ELF.string()`
- [#1057][1057] Fix a variable name typo in `DynELF` logging which results in an exception being thrown
- [#1058][1058] Fix an edge case in `ssh_process.exe`

[1007]: https://github.com/Gallopsled/pwntools/pull/1007
[1055]: https://github.com/Gallopsled/pwntools/pull/1055
[1057]: https://github.com/Gallopsled/pwntools/pull/1057
[1058]: https://github.com/Gallopsled/pwntools/pull/1058

## 3.9.2

- [#1043][1043] Do not attempt to populate the libraries used by statically-linked binaries

[1043]: https://github.com/Gallopsled/pwntools/pull/1043

## 3.9.1

- [#1038][1038] Fix an issue with `process()` where glibc would buffer data internally, causing a hang on `select()`
- [#1036][1036] Fix Travis CI logging verbosity
- [#1029][1029] Fix some `unicode` issues when using the `readline` command history in `tube.interactive()`

[1038]: https://github.com/Gallopsled/pwntools/pull/1038
[1036]: https://github.com/Gallopsled/pwntools/pull/1036
[1029]: https://github.com/Gallopsled/pwntools/pull/1029

## 3.9.0

- [#1003][1003] Make `concat_all` faster while also simplifying it's logic
- [#1014][1014] Fix for overwritten env when parsing core file
- [#1023][1023] Fixes to Travis CI

[1003]: https://github.com/Gallopsled/pwntools/pull/1003
[1014]: https://github.com/Gallopsled/pwntools/pull/1014
[1023]: https://github.com/Gallopsled/pwntools/pull/1023

## 3.8.0

- [#981][981] Fixed RELRO detection logic
- [#986][986] Enhancements to DynELF for controlling usage of LibcDB
- A few documentation fixes
- A few fixes for the Docker image

[981]: https://github.com/Gallopsled/pwntools/pull/981
[986]: https://github.com/Gallopsled/pwntools/pull/986

## 3.7.1

- [#998][998] Fix a bug where integer values could not be set in `.pwn.conf`.

[998]: https://github.com/Gallopsled/pwntools/pull/998

## 3.7.0

- [#933][933] DynELF works better with different base addresses
- [#952][952] A few small fixes were made to `pwn template`, and the CRC database was updated.
- [5c72d62c][5c72d62c] Updated the CRC database

[933]: https://github.com/Gallopsled/pwntools/pull/933
[952]: https://github.com/Gallopsled/pwntools/pull/952
[5c72d62c]: https://github.com/Gallopsled/pwntools/commit/5c72d62c

## 3.6.1

- [#979][979]+[1a4a1e1][1a4a1e1] Fixed [#974][974], a bug related to the terminal handling and numlock.
- [#980][980] Fixed the `pwn template` command.

[974]: https://github.com/Gallopsled/pwntools/issues/974
[979]: https://github.com/Gallopsled/pwntools/pull/979
[980]: https://github.com/Gallopsled/pwntools/pull/980
[1a4a1e1]: https://github.com/Gallopsled/pwntools/commit/1a4a1e1

## 3.6.0

- [#895][895] Added a Dockerfile to simplify testing setup and allow testing on OSX
- [#897][897] Fixed some incorrect AArch64 syscals
- [#893][893] Added the `pwnlib.config` module
    + Configuration options can now be set in `~/.pwn.conf`
    + This replaces the old, **undocumented** mechanism for changing logging colors.  Only @br0ns and @ebeip90 were likely using this.
    + More information is available in the documentation [here](http://docs.pwntools.com/en/dev/config.html).
- [#899][899] Pwntools now uses Unicorn Engine to emulate PLT instructions to ensure correct mapping of PIE / RELRO binaries.
- [#904][904] Enhancements to the accuracy of the `pwn checksec` command.
- [#905][905] Added a `pwn debug` command-line utility which automates the process of `gdb.attach(process(...))` to spawn GDB
    + More information is available in the documentation [here](http://docs.pwntools.com/en/dev/commandline.html#pwn-debug)
- [#919][919] Added a `pwn template` command-line utility to simplify the process of bootstrapping a new exploit.
    + More information is available in the documentation [here](http://docs.pwntools.com/en/dev/commandline.html#pwn-template).
- [#948][948] Fix unnecessary warning for Core files
- [#954][954] Fix list processing in `~/.pwn.conf`
- [#967][967] Respect `TERM_PROGRAM` for `run_in_new_terminal`
- [#970][970] Fix overly-aggressive corefile caching

[947]: https://github.com/Gallopsled/pwntools/pull/947
[948]: https://github.com/Gallopsled/pwntools/pull/948
[954]: https://github.com/Gallopsled/pwntools/pull/954
[960]: https://github.com/Gallopsled/pwntools/pull/960
[967]: https://github.com/Gallopsled/pwntools/pull/967
[968]: https://github.com/Gallopsled/pwntools/pull/968
[970]: https://github.com/Gallopsled/pwntools/pull/970

[895]: https://github.com/Gallopsled/pwntools/pull/895
[897]: https://github.com/Gallopsled/pwntools/pull/897
[893]: https://github.com/Gallopsled/pwntools/pull/893
[899]: https://github.com/Gallopsled/pwntools/pull/899
[904]: https://github.com/Gallopsled/pwntools/pull/904
[905]: https://github.com/Gallopsled/pwntools/pull/905
[919]: https://github.com/Gallopsled/pwntools/pull/919

## 3.5.1

- [#945][945] Speed up ssh via caching checksec results (fixes [#944][944])
- [#950][950] Fixes a bug where setting `context.arch` does not have an effect on `adb.compile()` output architecture

[944]: https://github.com/Gallopsled/pwntools/issues/944
[945]: https://github.com/Gallopsled/pwntools/pull/945
[950]: https://github.com/Gallopsled/pwntools/pull/950

## 3.5.0

- [b584ca3][b584ca3] Fixed an issue running `setup.py` on ARM
- [#822][822] Enabled relative leaks with `MemLeak`
    + This should be useful for e.g. heap-relative leaks
- [#832][832] Changed all internal imports to use absolute imports (no functional changes)
- [a12d0b6][a12d0b6] Move `STDOUT`, `PIPE`, `PTY` constants to globals
    + `process(..., stdin=process.PTY)` --> `process(..., stdin=PTY)`
- [#828][828] Use `PR_SET_PTRACER` for all `process()` and `ssh.process()` instances
    + This simplifies debugging on systems with YAMA ptrace enabled
- Various documentation enhancements
    + In particular, the [gdb][gdb], [elf][elf], and [ssh][ssh] docs are much better
- [#833][833] Performance enhancements for `adb` module
- [d0267f3][d0267f3] `packing.fit()` now treats large offsets as cyclic patterns (e.g. `0x61616161` behaves the same as `"aaaa"`)
- [#835][835] Added `ssh.checksec`
    + Reports the kernel version and other relevant information on connection
- [#857][857] Slightly shortened `execve` shellcode
- [300f8e0][300f8e0] Slightly speed up processing of large ELF files
- [#861][861] Adds support for extracting `IKCONFIG` configs from Linux kernel images, and extends `checksec` to report on any insecure configurations discovered
- [#871][871] Moves all of the basic syscall templates to `shellcraft/common` and exposes them via symlinks.  Closed [#685][685]
    + Should not have any visible effects from any documented APIs
    + `shellcraft.arch.os.syscall_function()` still works the same
    + We now have the ability to differentiate between the `connect` syscall, and a TCP `connect` helper
- [#887][887] `sh_string` now returns a quoted empty string `''` rather than just an empty string
- [#839][839] Exposes a huge amount of functionality via corefiles which was not previously availble.  See the [docs][corefile_docs] for examples.
    + `process().corefile` will automatically instantiate a Corefile for the process
    + QEMU-emulated processes are supported
    + Native processes are supported, including extraction of coredumps from `apport` crash logs
    + Native processes can be dumped *while running*, in a manner similar to `GDB`'s `gcore` script
- [#875][857] Added [documentation][aarch64] (and tests) for AArch64 shellcode
- [#882][882] The `ROP` class now respects `context.bytes` instead of using the hard-coded value of `4` (fixed [#879][879])
- [#869][869] Added several fields to the `process` class (`uid`, `gid`, `suid`, `sgid`) which are recorded at execution time, based on the file permissions
- [#868][868] Changed the way that `ssh.process()` works internally, and it now returns a more specialized class, `ssh_process`.
    + Added `ssh_process.corefile` for fetching remote corefiles
    + Added `ssh_process.ELF` for getting an ELF of the remote executable
    + The `uid`, `gid`, and `suid`, and `sgid` which are recorded at execution time, based on the file permissions
- [#865][865] Fixes `ELF.read` to support contiguous memory reads across non-contiguous file-backed segments
- [#862][862] Adds a `symlink=` argument to `ssh.set_working_directory`, which will automatically symlink all of the files in the "old" working directory into the "new" working directory

[ssh]: http://docs.pwntools.com/en/dev/tubes/ssh.html
[gdb]: http://docs.pwntools.com/en/dev/gdb.html
[elf]: http://docs.pwntools.com/en/dev/elf.html
[corefile_docs]: http://docs.pwntools.com/en/dev/elf/corefile.html
[aarch64]: http://docs.pwntools.com/en/dev/shellcraft/aarch64.html

[685]: https://github.com/Gallopsled/pwntools/pull/685
[822]: https://github.com/Gallopsled/pwntools/pull/822
[828]: https://github.com/Gallopsled/pwntools/pull/828
[832]: https://github.com/Gallopsled/pwntools/pull/832
[833]: https://github.com/Gallopsled/pwntools/pull/833
[835]: https://github.com/Gallopsled/pwntools/pull/835
[839]: https://github.com/Gallopsled/pwntools/pull/839
[857]: https://github.com/Gallopsled/pwntools/pull/857
[861]: https://github.com/Gallopsled/pwntools/pull/861
[862]: https://github.com/Gallopsled/pwntools/pull/862
[865]: https://github.com/Gallopsled/pwntools/pull/865
[868]: https://github.com/Gallopsled/pwntools/pull/868
[869]: https://github.com/Gallopsled/pwntools/pull/869
[871]: https://github.com/Gallopsled/pwntools/pull/871
[875]: https://github.com/Gallopsled/pwntools/pull/857
[879]: https://github.com/Gallopsled/pwntools/issues/879
[882]: https://github.com/Gallopsled/pwntools/pull/882
[887]: https://github.com/Gallopsled/pwntools/pull/887


[b584ca3]: https://github.com/Gallopsled/pwntools/commit/b584ca3
[a12d0b6]: https://github.com/Gallopsled/pwntools/commit/a12d0b6
[d0267f3]: https://github.com/Gallopsled/pwntools/commit/d0267f3
[300f8e0]: https://github.com/Gallopsled/pwntools/commit/300f8e0

## 3.4.1

- [#894][894] Fix a bug when using `gdb.debug()` over ssh.
- [e021f57][e021f57] Fix a bug ([#891][891]) in `rop` when needing to insert padding to fix alignment

[e021f57]: https://github.com/Gallopsled/pwntools/commit/e021f57
[894]: https://github.com/Gallopsled/pwntools/pull/894
[891]: https://github.com/Gallopsled/pwntools/issues/891

## 3.4.0

- [#800][800] Add `shell=` option to `ssh.process()`
- [#806][806] Add `context.buffer_size` for fine-tuning `tube` performance
    + Also adds `buffer_fill_size=` argument for all tubes
- [b83a6c7][b83a6c7] Fix undocumented `process.leak` function
- [546061e][546061e] Modify `coredump_filter` of all spawned processes, so that core dumps are more complete
- [#809][809] Add several functions to `adb` (`unlink`, `mkdir`, `makedirs`, `isdir`, `exists`)
- [#817][817] Make disconnection detection more robust

[800]: https://github.com/Gallopsled/pwntools/pull/800
[806]: https://github.com/Gallopsled/pwntools/pull/806
[809]: https://github.com/Gallopsled/pwntools/pull/809
[817]: https://github.com/Gallopsled/pwntools/pull/817
[5d9792f]: https://github.com/Gallopsled/pwntools/commit/5d9792f
[b83a6c7]: https://github.com/Gallopsled/pwntools/commit/b83a6c7
[546061e]: https://github.com/Gallopsled/pwntools/commit/546061e

## 3.3.4

- [#850][850] and [#846][846] fix issues with `hexdump` and the `phd` command-line utility, when using pipes (e.g. `echo foo | phd`)
- [#852][852] Fixes register ordering in `regsort`
- [#853][853] Fixes the registers restored in `shellcraft.amd64.popad`

[846]: https://github.com/gallopsled/pwntools/pull/846
[850]: https://github.com/gallopsled/pwntools/pull/850
[852]: https://github.com/gallopsled/pwntools/pull/852
[853]: https://github.com/gallopsled/pwntools/pull/853

## 3.3.3

- [#843][843] fixed a bug in `amd64.mov`.

[843]: https://github.com/gallopsled/pwntools/pull/843

## 3.3.2

- [#840][840] fixed a regression introduced by [#837][837].

[840]: https://github.com/gallopsled/pwntools/pull/840

## 3.3.1

- [#833][833] Fixed a performance-impacting bug in the adb module.
- [#837][837] Fixed a bug([#836][836]) causing `hexdump(cyclic=True)` to throw an exception.

[833]: https://github.com/Gallopsled/pwntools/pull/833
[837]: https://github.com/Gallopsled/pwntools/pull/837
[836]: https://github.com/Gallopsled/pwntools/issues/836

## 3.3.0

- [b198ec8][b198ec8] Added `tube.stream()` function, which is like `tube.interact()` without a prompt or keyboard input.
    + Effectively, this is similar to `cat file` and just prints data as fast as it is received.
- [aec3fa6][aec3fa6] Disable update checks against GitHub
    + These checks frequently broke due to GitHub query limits
- [#757][757] Fixed `adb.wait_for_device()` re-use of the same connection
- [f9133b1][f9133b1] Add a `STDERR` magic argument to make logging go to `stderr` instead of `stdout`
    + Usage is e.g. `python foo.py STDERR` or `PWNLIB_STDERR=1 python foo.py`
    + Also adds `context.log_console` to log to any file or terminal
- [67e11a9][67e11a9] Add faster error checking to `cyclic()` when provided very large values
- [5fda658][5fda658] Expose BitPolynom in `globals()`
- [#765][765] Added `-d` option for hex-escaped output for `shellcraft` command-line tool
- [#772][772] Fixed bash completion regressions
- [30c34b7][30c34b7] Fix `ROP.call()` with `Function` objects from `ELF.functions`
- [fa402ce][fa402ce] Add `adb.uptime` and `adb.boot_time`
- [82312ba][82312ba] Add `cyclic_metasploit` and `cyclic_metasploit_find`

[757]: https://github.com/Gallopsled/pwntools/pull/757
[765]: https://github.com/Gallopsled/pwntools/pull/765
[772]: https://github.com/Gallopsled/pwntools/pull/772
[b198ec8]: https://github.com/Gallopsled/pwntools/commit/b198ec8
[aec3fa6]: https://github.com/Gallopsled/pwntools/commit/aec3fa6
[f9133b1]: https://github.com/Gallopsled/pwntools/commit/f9133b1
[67e11a9]: https://github.com/Gallopsled/pwntools/commit/67e11a9
[5fda658]: https://github.com/Gallopsled/pwntools/commit/5fda658
[30c34b7]: https://github.com/Gallopsled/pwntools/commit/30c34b7
[fa402ce]: https://github.com/Gallopsled/pwntools/commit/fa402ce
[82312ba]: https://github.com/Gallopsled/pwntools/commit/82312ba

## 3.2.1

Multiple bug fixes.

- [#783][783] Fix `adb.uninstall` typo
- [#787][787] Added error handling for `ssh.process` argument `preexec_fn`
- [#793][793] Fixed progress message in `remote()` when connections failed
- [#802][802] Fixed partition listing in `adb.partitions`, which accidentally shelled out to the `adb` binary
- [#804][804] Fix error message for 32-bit distributions
- [#805][805] Fix exception in `Core.segments` when a segment has no name
- [#811][811] Fixes and performance improvements for `adb.wait_for_device()`
- [#813][813] Fixed a release script
- [#814][814] Fixed exceptions thrown if the `$HOME` directory is not writable
- [#815][815] Properly handle `None` in `MemLeak`

[783]: https://github.com/Gallopsled/pwntools/pull/783
[787]: https://github.com/Gallopsled/pwntools/pull/787
[793]: https://github.com/Gallopsled/pwntools/pull/793
[802]: https://github.com/Gallopsled/pwntools/pull/802
[804]: https://github.com/Gallopsled/pwntools/pull/804
[805]: https://github.com/Gallopsled/pwntools/pull/805
[811]: https://github.com/Gallopsled/pwntools/pull/811
[813]: https://github.com/Gallopsled/pwntools/pull/813
[814]: https://github.com/Gallopsled/pwntools/pull/814
[815]: https://github.com/Gallopsled/pwntools/pull/815

## 3.2.0

- [#695][695] Fixed a performance regression in `phd`.
- [452605e][452605e] Fixed [#629][629] related to correct removal of temporary files.
- [ea94ee4][ea94ee4] Disallows semi-colons in for the `run_in_terminal` function, since it did not work properly in all cases.
- [6376d07][6376d07] Added the mips shellcode `pushstr_array`.
- [#700][700] Added missing MIPS shellcode documentation to readthedocs, and enabled unit tests
- [#701][701] Command line tools refactored to have a common `pwn` entry point.
    + Added an option to *not* install the traditional `asm`, `disasm`, `checksec`, etc scripts
    + All existing tools can be accessed from the `pwn` command (e.g. `pwn asm nop`).
- [#704][704] The `process` object has a new, optional argument `alarm` for setting a `SIGALRM` timeout for processes.
- [#705][705] Added the Android Emulator to the test suite and Travis CI.
    + Android Emulator is now required for the full test suite
    + Android Emulator tests are skipped if no Android-related changes are detected
- [#711][711] `DynELF` has a new attribute, `heap`, which leaks the current `brk` address (heap base).  This is useful for finding heap allocations with dlmalloc-derived allocators like those used by Glibc.
- [#717][717] `sh_string` was rewritten to emit more compact and compatible strings
    + This was achieved by embedding single-quoted non-printable literals
    + Much more testing was added
    + Emitted strings are no longer copy-paste compatible, but work fine with e.g. `tubes` module and the default `subprocess` module
- [#709][709] The `adb` module now directly talks to the `adb` server process via a new module, `adb.protocol`
    + Removes the need to shell out to `adb`
    + Avoids version-compatibility issues with `adb` server vs. client
- [#703][703] Added new methods to `adb`
    + `install` - Installs an APK
    + `uninstall` - Uninstalls a package
    + `packages` - Lists installed packages
- [4893819][4893819] Modified `shellcraft.sh` on all platforms to provide `argv[0]` and set `argc==1`
    + This is needed for systems which have Busybox or other minimal shell for `/bin/sh` which does not behave well with `argc==0` or `argv[0]==NULL`.
- [1e414af][1e414af] Added `connect()` alias for `remote()`
    + For example, `io=connect('google.com', 80)`
    + This also works with `tcp(...)` and `udp(...)` aliases
- [869ec42][869ec42] Added `ssh.read()` and `ssh.write()` aliases
- [2af55c9][2af55c9] `AdbDevice` objects exposed via e.g. `adb.devices()` now offer scoped access to all `adb` module properties
    + It is now possible to e.g. `map(lambda d: d.process(['id']).recvall(), adb.devices())`


[629]: https://github.com/Gallopsled/pwntools/issues/629
[695]: https://github.com/Gallopsled/pwntools/pull/695
[700]: https://github.com/Gallopsled/pwntools/pull/700
[701]: https://github.com/Gallopsled/pwntools/pull/701
[704]: https://github.com/Gallopsled/pwntools/pull/704
[711]: https://github.com/Gallopsled/pwntools/pull/711
[717]: https://github.com/Gallopsled/pwntools/pull/717
[709]: https://github.com/Gallopsled/pwntools/pull/709
[705]: https://github.com/Gallopsled/pwntools/pull/705
[703]: https://github.com/Gallopsled/pwntools/pull/703
[452605e]: https://github.com/Gallopsled/pwntools/commit/452605e854f4870ef5ccfdf7fb110dfd75c50feb
[ea94ee4]: https://github.com/Gallopsled/pwntools/commit/ea94ee4ca5a8060567cc9bd0dc33796a89ad0b95
[6376d07]: https://github.com/Gallopsled/pwntools/commit/6376d072660fb2250f48bd22629bbd7e3c61c758
[1e414af]: https://github.com/Gallopsled/pwntools/commit/1e414afbeb3a01242f4918f111febaa63b640eb7
[869ec42]: https://github.com/Gallopsled/pwntools/commit/869ec42082b4b98958dfe85103da9b101dde7daa
[4893819]: https://github.com/Gallopsled/pwntools/commit/4893819b4c23182da570e2f4ea4c14d73af2c0df
[2af55c9]: https://github.com/Gallopsled/pwntools/commit/2af55c9bc382eca23f89bc0abc7a07c075521f94

## 3.1.1

Fixed a bug in `MemLeak.struct` (PR: #768).

## 3.1.0

A number of smaller bugfixes and documentation tweaks.

## 3.0.4

- Fixed a bug that made 3.0.3 uninstallable (Issue: #751, PR: #752)

## 3.0.3

- Fixed some performance and usability problems with the update system (Issues:
  #723, #724, #736. PRs: #729, #738, #747).
- Fixed a bug related to internals in pyelftools (PRs: #730, #746).
- Fixed an issue with travis (Issue: #741, PRs: #743, #744, #745).

## 3.0.2

- Cherry-pick #695, as this was a regression-fix.
- Added a fix for the update checker, as it would suggest prereleases as updates to stable releases.
- Various documentation fixes.

## 3.0.1

A small bugfix release. There were a lot of references to the `master`-branch, however after 3.0.0 we use the names `stable`, `beta` and `dev` for our branches.

## 3.0.0

This was a large release (1305 commits since 2.2.0) with a lot of bugfixes and changes.  The Binjitsu project, a fork of Pwntools, was merged back into Pwntools.  As such, its features are now available here.

As always, the best source of information on specific features is the comprehensive docs at https://pwntools.readthedocs.org.

This list of changes is non-complete, but covers all of the significant changes which were appropriately documented.

#### Android

Android support via a new `adb` module, `context.device`, `context.adb_host`, and `context.adb_port`.

#### Assembly and Shellcode

- Assembly module enhancements for making ELF modules from assembly or pre-assembled shellcode.  See `asm.make_elf` and `asm.make_elf_from_assembly`.
- `asm` and `shellcraft` command-line tools support flags for the new shellcode encoders
- `asm` and `shellcraft` command-line tools support `--debug` flag for automatically launching GDB on the result
- Added MIPS, PowerPC, and AArch64 support to the `shellcraft` module
- Added Cyber Grand Challenge (CGC) support to the `shellcraft` module
- Added syscall wrappers for every Linux syscall for all supported architectures to the `shellcraft` module
    + e.g. `shellcraft.<arch>.gettimeofday`
- (e.g. `shellcraft.i386.linux.`)
- Added in-memory ELF loaders for most supported architectures
    + Only supports statically-linked binaries
    + `shellcraft.<arch>.linux.loader`

#### Context Module

- Added `context.aslr` which controls ASLR on launched processes.  This works with both `process()` and `ssh.process()`, and can be specified per-process with the `aslr=` keyword argument.
- Added `context.binary` which automatically sets all `context` variables from an ELF file.
- Added `context.device`, `context.adb`, `context.adb_port`, and `context.adb_host` for connecting to Android devices.
- Added `context.kernel` setting for SigReturn-Oriented-Programming (SROP).
- Added `context.log_file` setting for sending logs to a file.  This can be set with the `LOG_FILE` magic command-line option.
- Added `context.noptrace` setting for disabling actions which require `ptrace` support.  This is useful for turning all `gdb.debug` and `gdb.attach` options into no-ops, and can be set via the `NOPTRACE` magic command-line option.
- Added `context.proxy` which hooks all connections and sends them to a SOCKS4/SOCKS5.  This can be set via the `PROXY` magic command-line option.
- Added `context.randomize` to control randomization of settings like XOR keys and register ordering (default off).
- Added `context.terminal` for setting how to launch commands in a new terminal.

#### DynELF and MemLeak Module

- Added a `DynELF().libc` property which attempt to find the remote libc and download the ELF from LibcDB.
- Added a `DynELF().stack` property which leaks the `__environ` pointer from libc, making it easy to leak stack addresses.
- Added `MemLeak.String` and `MemLeak.NoNewlines` and other related helpers for handling special leakers which cannot e.g. handle newlines in the leaked addresses and which leak a C string (e.g. auto-append a `'\x00'`).
- Enhancements for leaking speed via `MemLeak.compare` to avoid leaking an entire field if we can tell from a partial leak that it does not match what we are searching for.

#### Encoders Module

- Added a `pwnlib.encoders` module for assembled-shellcode encoders/decoders
- Includes position-independent basic XOR encoders
- Includes position-independent delta encoders
- Includes non-position-independent alphanumeric encoders for Intel
- Includes position-independent alphanumeric encoders for ARM/Thumb

#### ELF Module

- Added a `Core` object which can parse core-files, in order to extract / search for memory contents, and extract register states (e.g. `Core('./corefile').eax`).

#### Format Strings

- Added a basic `fmtstr` module for assisting with Format String exploitation

#### GDB Module

- Added support for debugging Android devices when `context.os=='android'`
- Added helpers for debugging shellcode snippets with `gdb.debug_assembly()` and `gdb.debug_shellcode()`

#### ROP Module

- Added support for SigReturn via `pwnlib.rop.srop`
    + Occurs automatically when syscalls are invoked and a function cannot be found
    + SigReturn frames can be constructed manually with `SigreturnFrame()` objects
- Added functional doctests for ROP and SROP

#### Tubes Process Module

- `process()` has many new options, check out the documentation
    + `aslr` controls ASLR
    + `setuid` can disable the effect of setuid, allowing core dumps (useful for extracting crash state via the new `Core()` object)
    + TTY echo and control characters can be enabled via `raw` argument
- `stdout` and `stderr` are now PTYs by default
    + `stdin` can be set to a PTY also via setting `stdin=process.PTY`

#### Tubes SSH Module

- Massive enhancements all over
- `ssh` objects now have a `ssh.process()` method which avoids the need to handle shell expansion via the old `ssh.run()` method
- Files are downloaded via SFTP if available
- New `download` and `upload` methods auto-detect whether the target is a file or directory and acts accordingly
- Added `listen()` method alias for `listen_remote()`
- Added `remote()` method alias for `connect_remote()`

#### Utilities

- Added `fit()` method to combine the functionality of `flat()` with the functionality of `cyclic()`
- Added `negative()` method to negate the value of an integer via two's complement, with respect to the current integer size (`context.bytes`).
- Added `xor_key()` method to generate an XOR key which avoids undesirable bytes over a given input.
- Added a multi-threaded `bruteforce()` implementation, `mbruteforce()`.
- Added `dealarm_shell()` helper to remove the effects of `alarm()` after you've popped a shell.

## 2.2.0

This was a large release with a lot of bugfixes and changes. Only the most significant
are mentioned here.

- Added shellcodes
- Added phd
- Re-added our expansion of itertools
- Added replacements for some semi-broken python standard library modules
- Re-implemented the rop module
- Added a serial tube
- Huge performance gains in the buffering for tubes
- Re-added user agents
- Begun using Travis CI with lots of test
- Removed bundled binutils in favor of documenting how to build them yourselves
- Added support for port forwarding though our SSH module
- Added dependency for capstone and ropgadget
- Added a lots of shellcodes
- Stuff we forgot
- Lots of documentation fixes
- Lots of bugfixes
