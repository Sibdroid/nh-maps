import matplotlib.pyplot as plt
import matplotlib.colors


def get_colormap(start_value: int,
                 end_value: int,
                 colors: list[str]):
    norm = plt.Normalize(start_value, end_value)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    return cmap


def tuple_to_hex(tpl: tuple) -> str:
    colors = [int(i*255) for i in tpl[:-1]]
    return "#"+"".join([hex(i)[2:].zfill(2) for i in colors])


def main() -> None:
    norm = plt.Normalize(-2, 2)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("",
                                                               ["red",
                                                                "blue"])
    print(tuple_to_hex(cmap(-2)))
    #cmap = get_colormap(80, 90, ["#3352a2", "#243c79"])
    #print([i*255 for i in cmap(80)])


if __name__ == "__main__":
    main()