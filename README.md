# anki-subs

Modified version of ["Watch Foreign Language Movies with Anki"](https://ankiweb.net/shared/info/939347702) to be used entirely in Anki, without external player while studying

Adds another note type with slightly different formatting and omitted script.

All credit to original creator ([repo](https://github.com/kelciour/movies2anki)), this is just a few modifications that I made for personal use

### Changes

- `movies2anki - alternative` note type within video card creation
  - Modified card template for viewing video within Anki desktop, as opposed to within mkv
  - `r` to replay video within card template
- Config changes to store in individual folder, and save as `.webm`

### Usage

Simply clone the repo into your `Anki/addons` folder, and the addon should be enabled upon an Anki restart

Follow the [original](https://ankiweb.net/shared/info/939347702) instructions to set up, and to use the custom note type, select `movies2anki - alternative` in the `Generate Video Cards` interface. Once cards are generated, run `Generate Mobile Cards` to create the appropriate `webm` files.

### To-Do

- Add more functionality to in-anki player, can bind buttons to modify html video info