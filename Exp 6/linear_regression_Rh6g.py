#Data from previous files
largest_area = [222043.87939700004, 133495.572454, 102815.22874300001, 85122.58972850002]
concentration = [0.0, 6.0, 12.0, 24.0]

intensity_ratio = []
for i in largest_area:
    intensity_ratio.append(largest_area[0]/i)

print(intensity_ratio)

import matplotlib.pyplot as plt

#X and Y values for regression
x_val = concentration
y_val = intensity_ratio

print(x_val)
print(y_val)

plt.plot(x_val, y_val, 'bo')
plt.title("Before regression")
plt.show()

import tensorflow as tf
import numpy as np

print(tf.__version__)

#TensorFlow graph
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1], kernel_initializer='glorot_uniform', bias_initializer='glorot_uniform')
])

#Loss function and the optimizer
loss_fn = tf.keras.losses.MeanSquaredError()
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=1000,
    decay_rate=0.9
)
optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)


# Train the model
model.compile(loss=loss_fn, optimizer=optimizer, metrics=['mse'])
for epoch in range(1001):
    loss, mse = model.train_on_batch(x_val, y_val)
    if epoch % 100 == 0:
        w, b = model.get_weights()
        print('Epoch %d: w = %f, b = %f, loss = %f' % (epoch, w[0][0], b[0], loss))

# Print the final weights and biases
w, b = model.get_weights()
print('w =', w[0][0])
print('b =', b[0])

# Compute R^2 value
y_mean = np.mean(y_val)
ss_tot = np.sum(np.square(y_val - y_mean))
y_pred = model.predict(x_val).flatten()
ss_res = np.sum(np.square(y_val - y_pred))
r2 = 1 - (ss_res / ss_tot)
print('R^2 value:', r2)

sample_x = np.linspace(0, 25, 1000)

plt.scatter(x_val, y_val, color = 'dimgray', label = 'raw data')
plt.plot(sample_x, sample_x * w[0][0] + b[0], color = 'royalblue', label = 'linear regression')

plt.title('Stern - Volmer plot', loc = 'center', pad = 15, fontsize = 15)
plt.legend(loc = 'best')

plt.xlabel("Concentration of NaI (mM)", labelpad = 15, fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity ratio", labelpad = 10, fontsize = 12, color = 'black', loc='center')

plt.text(15, 1.75, f"y = {w[0][0]:.3f}*x + {b[0]:.3f}" + "\n" + r'$R^{2}$ = ' + f"{r2:.3f}", fontsize = 11)


