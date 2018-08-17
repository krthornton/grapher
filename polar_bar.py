import numpy as np
import matplotlib.pyplot as plt


def render_graph(name, section_names, value_list, padding, max, size, font):
    # keep some constants for later
    N = len(value_list)  # how many slices are on the graph
    radii = value_list
    names = section_names

    # do some math stuff
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    width = np.pi / (N / 2)

    fig = plt.figure(figsize=(size, size))
    ax = fig.add_subplot(111, polar=True)
    bars = ax.bar(theta, radii, tick_label='', width=width, bottom=0.0)
    # bars = ax.bar(theta, radii, tick_label=names, width=width, bottom=0.0)

    # Use custom colors and opacity
    ax.grid(False)
    ax.set_yticklabels([])
    ax.set_xticklabels(names)
    plt.ylim(0, float(max))
    for r, bar in zip(range(N), bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)

    plt.gcf().canvas.draw()
    angles = np.linspace(0, 2 * np.pi, len(ax.get_xticklabels()) + 1)
    angles[np.cos(angles) < 0] = angles[np.cos(angles) < 0] + np.pi
    angles = np.rad2deg(angles)
    labels = []
    count = 0

    for label, angle in zip(ax.get_xticklabels(), angles):
        x, y = label.get_position()
        if count <= (len(names) / 4):
            lab = ax.text(x, y, label.get_text(),
                          transform=label.get_transform(),
                          ha='left', va='bottom',
                          size=font)
            lab.set_rotation(angle)
            labels.append(lab)
        elif (len(names) / 4) < count <= (len(names) / 2):
            lab = ax.text(x, y, label.get_text(),
                          transform=label.get_transform(),
                          ha='right', va='bottom',
                          size=font)
            lab.set_rotation(angle)
            labels.append(lab)
        elif (len(names) / 2) < count <= ((3 / 4) * len(names)):
            lab = ax.text(x, y, label.get_text(),
                          transform=label.get_transform(),
                          ha='right', va='top',
                          size=font)
            lab.set_rotation(angle)
            labels.append(lab)
        else:
            lab = ax.text(x, y, label.get_text(),
                          transform=label.get_transform(),
                          ha='left', va='top',
                          size=font)
            lab.set_rotation(angle)
            labels.append(lab)
        count += 1
    ax.set_xticklabels([])

    if name != '':
        plt.title(name)

    try:
        plt.tight_layout(pad=padding)
    except ValueError:
        plt.close()
        return False
    else:
        plt.show()


if __name__ == '__main__':
    render_graph('Kaleb', ['one', 'areallybigword', 'threeeeeeeee', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2])