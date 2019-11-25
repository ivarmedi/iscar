ARG PYTHON_MAJOR_MINOR=3.7
FROM python:${PYTHON_MAJOR_MINOR}
ARG COCO_MODEL="ssd_mobilenet_v1_coco_2018_01_28"

WORKDIR /var/www/ivli_iscar

COPY requirements.txt ./requirements.txt

RUN python3 -m pip install --no-cache-dir --compile -r requirements.txt && \
    wget http://download.tensorflow.org/models/object_detection/${COCO_MODEL}.tar.gz && \
    tar zxvf ${COCO_MODEL}.tar.gz && \
    mv ${COCO_MODEL}/frozen_inference_graph.pb ./ && \
    rm -rf ${COCO_MODEL}*

ENV PYTHONPATH=/usr/lib/python3.7/site-packages

COPY . .

CMD [ "python", "server.py" ]
